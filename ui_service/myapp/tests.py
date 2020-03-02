# Create your tests here.
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve

from myapp.forms import PostForm
from myapp.models import Post
import json


### TEST DE URLS ###
class TestUrls(SimpleTestCase):
    
    def test_index(self):
        url = reverse('index')
        self.assertEquals(resolve(url).url_name,'index')

    def test_response(self):
        url = reverse('responses')
        self.assertEquals(resolve(url).url_name,'responses')


### TEST DE FORMS ###
class TestForms(SimpleTestCase):

    def test_post_form_no_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())

    def test_post_form_data(self):
        form = PostForm(data={'message':'hola mundo'})
        self.assertTrue(form.is_valid())


### TEST DE MODELOS ###
class TestModel(TestCase):

    def test_post(self):
        Post(content = "contenido").save()
        posts = Post.objects.all()
        post = Post.objects.get(id=1)
        self.assertEquals(posts.count(),1)
        self.assertEquals(post.content,"contenido")


### TEST DE VISTAS ###
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index = reverse('index')
        self.responses = reverse('responses')

        self.post = Post.objects.create(content = "prueba de vista")

    
    def test_view_index(self):
        response = self.client.get(self.index)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'myapp/home.html')

    def test_view_index_data(self):
        response = self.client.post(
            self.index,{'message':'prueba en vista index'}
            )
        self.assertEqual(response.status_code,200)

    def test_view_index_very_data(self):
        for  solicitud in range(1,100):
            response = self.client.post(
                self.index,{'message':'Solicitud: '+str(solicitud)}
                )
            self.assertEqual(response.status_code,200)