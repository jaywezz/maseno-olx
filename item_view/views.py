from django.shortcuts import render
from .models import Item, Comments
from authentication.models import DaemonStar_User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from  .forms import UploadItemForm,ItemEditForm, CartAddProductForm, CommentForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import View
from django.conf import settings
from django.views.decorators.http import require_POST
from .cart import Cart



def welcome_page(request):
	recommended_uploaded_items = Item.objects.all().order_by('-date_created')[10:16]
	first_recently_uploaded_item = Item.objects.all().order_by('-date_created')[:1]
	recently_uploaded_items = Item.objects.all().order_by('-date_created')[4:8]
	featured_uploaded_items = Item.objects.all().order_by('-date_created')[:3]

	return render(request, "new_templates/index.html", {'first_recently_uploaded_item': first_recently_uploaded_item,
																		 'featured_uploaded_items': featured_uploaded_items,
																		 'recently_uploaded_items': recently_uploaded_items,
																		 'recommended_uploaded_items': recommended_uploaded_items})

class UploadView(LoginRequiredMixin, View):
		login_url = 'authentication:sign_in'
		form_class = UploadItemForm
		template_name = 'Maseno_olx-template/upload.html'

		def get(self, request):
			form = self.form_class(None)
			return render(request, self.template_name, {'form': form})

		def post(self, request):
			form = self.form_class(request.POST, request.FILES)
			if form.is_valid:
				instance = form.save(commit=False)


				instance.item_owner = request.user
				instance.save()


				messages.success(request, "Successfully uploaded")

				print("data saved")

				return HttpResponseRedirect(instance.get_absolute_url())

			else:

				print('form is valid')

			return render(request, self.template_name, {'form': form})


def item_detail(request, name):
	uploaded_item = get_object_or_404(Item, item_name=name)
	comments = Comments.objects.filter(item=name)

	owner = get_object_or_404(DaemonStar_User, username=uploaded_item.item_owner)

	if request.method == 'POST':

			ItemEdit = ItemEditForm(
				instance=uploaded_item,
				data=request.POST,
				files=request.FILES)
			comment = CommentForm(data=request.POST)

			if ItemEdit.is_valid():

				ItemEdit.save()
				return redirect('item_view:item_detail', name=uploaded_item.item_name)

			if comment.is_valid():
				instance = comment.save(commit=False)
				instance.item = uploaded_item.item_name
				instance.save()
				redirect('item_view:item_detail', name=uploaded_item.item_name)



	else:
			redirect('item_view:item_detail', name=uploaded_item.item_name)
			ItemEdit = ItemEditForm(instance=uploaded_item)
			comment = CommentForm()



	cart_product_form = CartAddProductForm()
	if uploaded_item.item_owner == request.user:
		#return render(request, 'Maseno_olx-template/item_detail.html', {'form': form, 'item': uploaded_item})
		return render(request, 'new_templates/owner_item_detail.html', {'commentform': comment, 'comments': comments, 'form': ItemEdit, 'item': uploaded_item})

	else:
		return render(request, 'new_templates/user_item_detail.html', {'commentform': comment, 'comments': comments,  'item': uploaded_item, 'cart_priduct_form':cart_product_form,
																							 'owner':owner})


@require_POST
def cart_add(request, item_id):
	cart = Cart(request)

	item = get_object_or_404(Item, id=item_id)
	form = CartAddProductForm(request.POST)
	print(item_id)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(item=item, quantity=cd['quantity'], update_quantity=cd['update'])


	return redirect('item_view:cart_detail')

def cart_remove(request, item_id):
	cart = Cart(request)
	item = get_object_or_404(Item, id=item_id)
	cart.remove(item)
	return redirect('cart:cart_detail')


def cart_detail(request):
	cart_items = Cart(request)
	cart = cart_items.cart
	return render(request, 'Maseno_olx-template/cart_details.html', {'cart': cart})


