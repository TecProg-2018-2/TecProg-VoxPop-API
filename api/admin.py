"""
*********************************************************************
* File: admin.py
* Purpose: ExtendedUserAdmin,ParliamentaryAdmin, ParliamentaryVoteAdmin,
*   PropositionAdmin, SocialInformationAdmin,UserFollowingAdmin,
*   UserVoteAdmin, ContactUsAdmin class implementation
* Notice: All rights reserved.
* Description File: Registering a models with the admin site.
***********************************************************************/
"""

# models
from .models import (
    ContactUs, ExtendedUser, Parliamentary, ParliamentaryVote, Proposition,
    SocialInformation, UserFollowing, UserVote, 
)
# django
from django.contrib import admin

"""
Responsible class to register User
with admin site and describe the fields 
"""
class ExtendedUserAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'should_update'
    ]

"""
Responsible class to register Parliamentary 
with admin site and describe the fields 
"""
class ParliamentaryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'gender',
        'political_party',
        'federal_unit',
        'birth_date',
        'education',
        'email'
    ]

"""
Responsible class to register Parliamentary Vote
with admin site and describe the fields 
"""
class ParliamentaryVoteAdmin(admin.ModelAdmin):
    list_display = [
        'option',
        'proposition',
        'parliamentary'
    ]

"""
Responsible class to register Proposition
with admin site and describe the fields 
"""
class PropositionAdmin(admin.ModelAdmin):
    list_display = [
        'proposition_type',
        'proposition_type_initials',
        'number',
        'year',
        'abstract',
        'processing',
        'situation',
        'last_update'
    ]

"""
Responsible class to register Social Information 
with admin site and describe the fields 
"""
class SocialInformationAdmin(admin.ModelAdmin):
    list_display = [
        'owner',
        'region',
        'income',
        'education',
        'race',
        'gender',
        'birth_date',
    ]

"""
Responsible class to register User Following 
with admin site and describe the fields 
"""
class UserFollowingAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'parliamentary'
    ]

"""
Responsible class to register User Vote 
with admin site and describe the fields 
"""
class UserVoteAdmin(admin.ModelAdmin):
    list_display = [
        'option',
        'proposition',
        'user'
    ]

"""
Responsible class to register Contact Us 
with admin site and describe the fields 
"""
class ContactUsAdmin(admin.ModelAdmin):
    list_display = [
        'topic',
        'email',
        'choice',
        'text'
    ]

"""
Register admin for each model
"""
admin.site.register(ExtendedUser, ExtendedUserAdmin)
admin.site.register(Parliamentary, ParliamentaryAdmin)
admin.site.register(ParliamentaryVote, ParliamentaryVoteAdmin)
admin.site.register(Proposition, PropositionAdmin)
admin.site.register(SocialInformation, SocialInformationAdmin)
admin.site.register(UserFollowing, UserFollowingAdmin)
admin.site.register(UserVote, UserVoteAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
