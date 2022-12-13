import io
from pathlib import Path

from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image


def converter(obj):
    """Функция конвертации формата изображений в webp."""
    new_file_name = str(Path(obj.name).with_suffix('.webp'))
    image = Image.open(obj.file)
    thumb_io = io.BytesIO()
    image.save(thumb_io, 'webp', optimize=True, quality=95)
    new_obj = InMemoryUploadedFile(
        thumb_io,
        obj.name,
        new_file_name,
        size=obj.size,
        charset='utf-8',
        content_type='image/jpeg',
    )
    return new_obj
