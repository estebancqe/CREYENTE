import reflex as rx

class Swiper(rx.Component):
    library = "swiper/react"
    tag = "Swiper"
    
    lib_dependencies: list[str] = [
        "swiper",
    ]

    def get_custom_code(self) -> str:
        return """
        import 'swiper/swiper-bundle.min.css';
        """

class SwiperSlide(rx.Component):
    library = "swiper/react" 
    tag = "SwiperSlide"