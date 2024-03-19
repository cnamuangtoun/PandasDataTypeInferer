from django.shortcuts import render
from django.http import JsonResponse
from .models import ProcessedFile
from django.views.decorators.csrf import csrf_exempt
from .cleaner import read_and_convert



@csrf_exempt
def process_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        try:
            # Process the file
            processed_df = read_and_convert(uploaded_file)       
            data = processed_df.to_json(orient='records')
            data_types = processed_df.dtypes.apply(lambda x: str(x)).to_dict()
            
            print(processed_df)
            
            return JsonResponse({
                'processed_data': data,
                'data_types': data_types,
            })

        except Exception as e:
            print(str(e))
            return JsonResponse({'error': str(e)})

    return render(request, 'data_processor/upload.html')