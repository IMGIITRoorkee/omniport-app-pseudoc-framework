import datetime
import swapper

from django.utils import timezone

from open_auth.models import Application

def approve_application(data:dict):
    
    """
    Approve an application matching the provided filters.
    First tries to find a unique match using name and team members only.
    If multiple matches found, uses date_of_creation as additional filter on subsequent calls.
    
    Components of the dictionary:
        app_name (str): Application name (exact or partial match)
        team_members_list (list): Enrollment numbers of team members
        date_of_creation(datetime): Specific date when application was created
    
    Returns:
        tuple: (message, status_code)
    """

    app_name = data.get('app_name',None)
    team_members_list = data.get('team_members_list',None)
    date_of_creation= data.get('date_of_creation',None)
    try:
        queryset = Application.objects.all()
        if not app_name:
            return "Application name is required.", 400
        queryset = queryset.filter(name=app_name)
        if team_members_list:
            try:
                Person = swapper.load_model('kernel', 'Person')
                team_members = Person.objects.filter(
                    user__username__in=team_members_list
                )
                if not team_members.exists():
                    return "No team members found with the provided enrollment numbers.", 404
                for team_member in team_members:
                    queryset = queryset.filter(team_members=team_member)
            except Exception as e:
                return f"Error processing team members: {str(e)}", 500
        else:
            return "Team member enrollment numbers are required.", 400
        
        application_count = queryset.count()
        if application_count == 0:
            return "No matching applications found.", 404
        if application_count == 1:
            application = queryset.first()
            if application.is_approved: 
                return "Application is already approved.", 400
            application.is_approved = True
            application.save()
            return f"Successfully approved application: {application.name}", 200
        
        if application_count > 1 :
            return f"Found {application_count} matching applications. Please provide creation date to narrow results.", 300
        
        if date_of_creation:
            try:
                if isinstance(date_of_creation, str):
                    date_of_creation= datetime.datetime.strptime(date_of_creation, "%Y-%m-%d").date()
                
                start_date = datetime.datetime.combine(date_of_creation, datetime.time.min)
                end_date = datetime.datetime.combine(date_of_creation, datetime.time.max)
                
                if timezone.is_naive(start_date):
                    start_date = timezone.make_aware(start_date)
                if timezone.is_naive(end_date):
                    end_date = timezone.make_aware(end_date)
                    
                queryset = queryset.filter(
                    datetime_created__gte=start_date,
                    datetime_created__lte=end_date
                )
                if not queryset.exists():
                    return f"No applications found on {date_of_creation}.", 404
                
                if queryset.count() > 1:
                    return f"Found {queryset.count()} applications on {date_of_creation}. Please contact administrator.", 300
                application = queryset.first()
                application.is_approved = True
                application.save()
                return f"Successfully approved application: {application.name}", 200
                
            except ValueError:
                return "Invalid date format. Please use YYYY-MM-DD.", 400
            except Exception as e:
                return f"Error processing creation date: {str(e)}", 500
        else:
            return "Creation date is required to narrow down multiple matching applications.", 400
            
    except Exception as e:
        return f"Error approving application: {str(e)}", 500