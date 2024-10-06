from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import UpdateView
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from datetime import datetime
from .models import Location, Comment
from .forms import CommentForm, LocationForm


class LocationList(generic.ListView):
    """
    This class is the typical default list view, used
    to display the location posts in a grid list
    """
    model = Location
    queryset = Location.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'
    paginate_by = 6


class LocationSingle(View):
    """
    This class finds one location to display, using the slug
    to uniquely identify it from the query set
    """
    def get(self, request, location_slug, *args, **kwargs):
        queryset = Location.objects.filter(status=1)
        location = get_object_or_404(queryset, slug=location_slug)
        comments = location.comments.order_by('created_at')
        post_liked = False
        if location.likes.filter(id=self.request.user.id).exists():
            post_liked = True

        return render(
            request,
            "location_single.html",
            {
                "location": location,
                "comments": comments,
                "liked": post_liked,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, location_slug, *args, **kwargs):
        """
        This method enables creation of a new Location
        """
        queryset = Location.objects.filter(status=1)
        location = get_object_or_404(queryset, slug=location_slug)
        comments = location.comments.order_by('created_at')
        post_liked = False
        if location.likes.filter(id=self.request.user.id).exists():
            post_liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.location = location
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "location_single.html",
            {
                "location": location,
                "comments": comments,
                "liked": post_liked,
                "comment_form": CommentForm()
            }
        )


class LocationLike(View):
    """
    This class is used to allow users to like a location
    """
    def post(self, request, slug):
        """
        This method posts the like
        """
        location = get_object_or_404(Location, slug=slug)

        if location.likes.filter(id=request.user.id).exists():
            location.likes.remove(request.user)
        else:
            location.likes.add(request.user)

        return HttpResponseRedirect(reverse('location_single', args=[slug]))


class MyLocations(View):
    """
    This class allows display of locations uploaded by a user
    """
    def get(self, request):
        """
        This methods gets the list of locations
        """
        if request.user.is_authenticated:
            the_locations = Location.objects.filter(
                creator=request.user).order_by('-created_at')

            return render(
                request, 'my_locations.html', {"the_locations": the_locations})
        else:
            return render(request, 'my_locations.html')


class AddLocation(View):
    """
    This class enables the adding of a new location
    """
    def get(self, request):
        """
        Get method to load the location form
        """
        return render(
            request, "add_location.html", {"location_form": LocationForm()})

    def post(self, request):
        """ Post method to allow post a location """
        location_form = LocationForm(request.POST, request.FILES)

        if location_form.is_valid():
            location = location_form.save(commit=False)
            location.creator = request.user
            # Code to make slug unique using date time
            curr_time = datetime.now()
            date_time = curr_time.strftime("%m/%d/%Y%H:%M:%S")
            location.slug = slugify('-'.join([location.title, date_time]))
            location.save()
            return redirect('my_locations')
        else:
            location_form = LocationForm()

        return render(
            request,
            "add_location.html",
            {
                "location_form": location_form
            },
        )


class EditLocation(UpdateView):
    """ This class uses to default UpdateView to load
    the update location form """
    model = Location
    template_name = 'edit_location.html'
    form_class = LocationForm


def publish_location(request, location_id):
    """ This method enables a location to be published from draft version """

    location = get_object_or_404(Location, id=location_id)
    location.status = 1
    location.save()
    return redirect(reverse('home'))


def delete_location(request, location_id):
    """ This method enables a location to be deleted """
    location = get_object_or_404(Location, id=location_id)
    location.delete()
    return redirect(reverse('my_locations'))