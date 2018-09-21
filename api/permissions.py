"""
*********************************************************************
* File: permissions.py
* Purpose: UserPermissions, SocialInformationPermissions
*          class implementation
* Notice: All rights reserved.
* Description File: Configures permissions.
***********************************************************************/
"""

# rest_framework
from rest_framework import permissions

# models
from .models import SocialInformation

"""
Responsible class to configure 
user permissions
"""
class UserPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Method for setting user permissions.
        """
        permission_classes = False
        authorized_user = False

        """
        Configuration made according to the response obtained in the request.
        """
        if request.user.is_superuser:
            return True

        elif (request.user.is_anonymous and request.method == 'POST'):
            return True

        elif 'users' in request.path and 'actual_user' not in request.path:
            url_id = request.path.split('/users/')[1][:-1]
            user_id = str(request.user.id)

            if(url_id == user_id):
                authorized_user = True

            if(request.method != 'DELETE' and request.method != 'POST' and
                    authorized_user):
                return True

        else:
            permission_classes = True

        return permission_classes

"""
Responsible class to configure 
social information permissions
"""
class SocialInformationPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Method for setting social information permissions.
        """
        permission_classes = False
        authorized_user = False

        """
        Configuration made according to the response obtained in the request.
        """
        if request.user.is_superuser:
            return True

        elif request.user.is_anonymous:
            return False

        elif (request.method == 'POST' and
                SocialInformation.objects.filter(
                    owner=request.user
                ).count() == 0):
            return True

        elif 'social_informations' in request.path:

            social_information = \
                SocialInformation.objects.filter(owner=request.user.id)
            if(social_information):
                social_information = social_information.first().id
            url_id = request.path.split('/social_informations/')[1][:-1]

            if(url_id == str(social_information)):
                authorized_user = True

            if(request.method != 'DELETE' and authorized_user):
                return True

        else:
            permission_classes = True

        return permission_classes
