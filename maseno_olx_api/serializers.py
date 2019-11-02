
from item_view.models import Item
from authentication.models import DaemonStar_User
from rest_framework import serializers
from django.contrib.auth import authenticate


# Serializing the Items model
class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ['item_name', 'item_description', 'item_price', 'item_category', 'item_owner', 'date_created', 'item_image']

class UserSerializer(serializers.ModelSerializer):
	confirm_password = serializers.CharField()

	password = serializers.CharField(
		max_length=128,
		min_length=8,
		write_only=True
	)
	class Meta:
		model = DaemonStar_User
		fields = ['username', 'email', 'phone_number', 'location', 'password', 'confirm_password']


class LoginSerializer(serializers.Serializer):
	email = serializers.CharField(max_length=255)
	username = serializers.CharField(max_length=255, read_only=True)
	password = serializers.CharField(max_length=128, write_only=True)
	token = serializers.CharField(max_length=255, read_only=True)

	def validate(self, data):
	# The `validate` method is where we make sure that the current
   # instance of `LoginSerializer` has "valid". In the case of logging a
   # user in, this means validating that they've provided an email
   # and password and that this combination matches one of the users in
   # our database.

		email = data.get('email', None)
		password = data.get('password', None)
		if email is None:
				raise serializers.ValidationError(
                'An email address is required to log in.'
            )

		if password is None:
				raise serializers.ValidationError(
                'A password is required to log in.'
            )

		# The `authenticate` method is provided by Django and handles checking
		# for a user that matches this email/password combination. Notice how
		# we pass `email` as the `username` value since in our User
      # model we set `USERNAME_FIELD` as `email`.

		user = authenticate(username=email, password=password)

		# If no user was found matching this email/password combination then
		# `authenticate` will return `None`. Raise an exception in this case.
		if user is None:
			raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

		# Django provides a flag on our `User` model called `is_active`. The
		# purpose of this flag is to tell us whether the user has been banned
		# or deactivated. This will almost never be the case, but
		# it is worth checking. Raise an exception in this case.
		if not user.is_active:
			raise serializers.ValidationError(
                'This user has been deactivated.'
            )

		# The `validate` method should return a dictionary of validated data.
		# This is the data that is passed to the `create` and `update` methods
		# that we will see later on.
		return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }







