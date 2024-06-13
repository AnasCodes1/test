from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.db.models import Q

from .models import Book

class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "book/book_list.html"


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = Book
    context_object_name = "book"
    template_name = "book/book_detail.html"
    permission_required = "books.special_status"


class SearchResultListView(generic.ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "book/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )