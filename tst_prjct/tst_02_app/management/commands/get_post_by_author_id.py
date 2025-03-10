from django.core.management.base import BaseCommand
from tst_02_app.models import Post, Author


class Command(BaseCommand):
    help = "Get all posts by author id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    # def handle(self, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     author = Author.objects.filter(pk=pk).first()
    #     if author is not None:
    #         posts = Post.objects.filter(author=author)
    #     intro = f'All posts of {author.name}\n'
    #     text = '\n'.join(post.content for post in posts)
    #     self.stdout.write(f'{intro}{text}')

    # Если имя автора не требуется
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        posts = Post.objects.filter(author__pk=pk)
        intro = f'All posts\n'
        text = '\n'.join(post.content for post in posts)
        # text = '\n'.join(post.get_summary() for post in posts)  # Для вывода 8 слов из статьи
        self.stdout.write(f'{intro}{text}')
