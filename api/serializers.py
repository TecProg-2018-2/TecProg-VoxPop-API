from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

from .models import (
    Compatibility, ExtendedUser, Parliamentary, ParliamentaryVote, Proposition,
    SocialInformation, UserFollowing, UserVote, ContactUs
)

class SocialInformationSerializer(serializers.ModelSerializer):
#Model social informations about the user.

    class Meta:
        model = SocialInformation
        fields = [
            'id',
            'owner',
            'region',
            'income',
            'education',
            'race',
            'gender',
            'birth_date',
        ]

class UserSerializer(serializers.ModelSerializer):
    """
    Models relation between social informations adding user informations
    to use as a user id.
    """
    social_information = SocialInformationSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'social_information',
        ]

        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }

    def create(self, validated_data):
    #Create voxpopuser, validating its data.
        voxpopuser = User(**validated_data)
        password = validated_data['password']
        voxpopuser.set_password(password)
        voxpopuser.save()
        token = Token.objects.create(user=voxpopuser)
        token.save()
        extended_user = ExtendedUser.objects.create(user=voxpopuser)
        extended_user.save()
        return voxpopuser

    def update(self, instance, validated_data):
    #Update user, validating its data.
        updated_user = vars(instance)
        del updated_user['_state']
        for field, value in validated_data.items():
            updated_user[field] = value

        updated = User(**updated_user)
        if 'password' in validated_data:
            updated.set_password(validated_data['password'])

        updated.save()

        return updated

class ParliamentarySerializer(serializers.ModelSerializer):
#Models datas about the parliamentarians.

    class Meta:
        model = Parliamentary
        fields = [
            'id',
            'parliamentary_id',
            'name',
            'gender',
            'political_party',
            'federal_unit',
            'birth_date',
            'education',
            'email',
            'photo'
        ]

class PropositionSerializer(serializers.ModelSerializer):
#Models propositions related to the parliamentarians.

    class Meta:
        model = Proposition
        fields = [
            'id',
            'native_id',
            'proposition_type',
            'proposition_type_initials',
            'number',
            'year',
            'abstract',
            'processing',
            'situation',
            'url_full',
            'last_update'
        ]

class UserVoteSerializer(serializers.ModelSerializer):
#Models option vote for the user.

    class Meta:
        model = UserVote
        fields = [
            'id',
            'user',
            'proposition',
            'option'
        ]

class ParliamentaryVoteSerializer(serializers.ModelSerializer):
#Models option vote for the parliamentary.

    class Meta:
        model = ParliamentaryVote
        fields = [
            'id',
            'parliamentary',
            'proposition',
            'option'
        ]

class UserFollowingSerializer(serializers.ModelSerializer):
#Models relation of the parliamentarians and users.

    class Meta:
        model = UserFollowing
        fields = [
            'user',
            'parliamentary'
        ]

        extra_kwargs = {
            'user': {
                'write_only': True
            },
        }

class CompatibilitySerializer(serializers.ModelSerializer):
#Study about datas with the votes and the compatibility with the user.
    parliamentary = ParliamentarySerializer(many=False)

    class Meta:
        model = Compatibility
        fields = [
            'user',
            'parliamentary',
            'valid_votes',
            'matching_votes',
            'compatibility'
        ]

class ContactSerializer(serializers.ModelSerializer):
# Contact with the responsibles, sending data to a formulary.

    class Meta:
        model = ContactUs
        fields = [
            'id',
            'topic',
            'email',
            'choice',
            'text'
        ]
