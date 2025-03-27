import torchvision.transforms as T
from torchvision.transforms.functional import normalize


def convert_to_rgb(image):
    return image.convert("RGB")

def get_transform(image_size=384):
    return T.Compose([
        convert_to_rgb,
        T.Resize((image_size, image_size)),
        T.ToTensor(),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
