from django.shortcuts import render

class Click(generics.ListAPIView):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer    


class ClickCreate(generics.CreateAPIView):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer  
    

class ClickDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClickSerializer
    queryset = Click.objects.all()
