# services/cloudinary_service.py

import cloudinary.uploader


class CloudinaryService:

    @staticmethod
    def upload_file(
        file,
        public_id: str
    ):
        return cloudinary.uploader.upload(
            file=file,
            public_id=public_id,
            resource_type="raw",
            overwrite=False
        )

    @staticmethod
    def delete_file(
        public_id: str
    ):
        return cloudinary.uploader.destroy(
            public_id,
            resource_type="raw"
        )