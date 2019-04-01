from django.views import generic

from .models import Book


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if 'pub_date' in self.kwargs.keys():
            books_ordered = self.model.objects.order_by('pub_date')
            prev_book = books_ordered.filter(pub_date__lt=self.kwargs['pub_date']).last()
            next_book = books_ordered.filter(pub_date__gt=self.kwargs['pub_date']).first()

            if next_book:
                context['next'] = next_book.pub_date

            if prev_book:
                context['prev'] = prev_book.pub_date

        return context

    def get_queryset(self):
        if self.kwargs:
            return self.model.objects.filter(pub_date=self.kwargs['pub_date'])

        return self.model.objects.all().order_by('pub_date')
