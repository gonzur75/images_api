from images.validators import validate_file_type


def test_valid_image(image):
    assert not validate_file_type(image)
