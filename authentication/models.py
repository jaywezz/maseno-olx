
from django.db import models
from django.contrib.auth.models import AbstractUser
import jwt

from datetime import datetime, timedelta
from django.conf import settings


class DaemonStar_User(AbstractUser):
	location = models.CharField(max_length=100, null=True)
	phone_number = models.IntegerField(null=True)
	user_avatar = models.ImageField(upload_to="profiles", blank=True, default='/profiles/3.jpg')

	@property
	def token(self):
		"""
		Allows us to get a user's token by calling `user.token` instead of
		`user.generate_jwt_token().

		The `@property` decorator above makes this possible. `token` is called
		a "dynamic property".
		"""
		return self._generate_jwt_token()

	def _generate_jwt_token(self):
		"""
		Generates a JSON Web Token that stores this user's ID and has an expiry
		date set to 60 days into the future.
		"""
		dt = datetime.now() + timedelta(days=60)

		token = jwt.encode({
			'id': self.pk,
			'exp': int(dt.strftime('%s'))
		}, settings.SECRET_KEY, algorithm='HS256')

		return token.decode('utf-8')