from .models import Item, Comments, Replies

from django import forms



class UploadItemForm(forms.ModelForm):

	class Meta:
		model = Item
		fields = ('item_name', 'item_description', 'item_price', 'item_image', 'item_category')

class ItemEditForm(forms.ModelForm):

	class Meta:
		model = Item
		fields = ('item_description', 'item_price', 'item_image', 'item_category')

ITEM_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
	quantity = forms.TypedChoiceField(choices=ITEM_QUANTITY_CHOICES, coerce=int)
	update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comments
		fields = ('comment', 'full_name', 'email', 'phone_number')


