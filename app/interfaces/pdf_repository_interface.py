from abc import ABC, abstractmethod


class PDFRepositoryInterface(ABC):
    """
    Interface for PDF repository
    """

    @abstractmethod
    def load_pdf(self, file_path):
        pass

    @abstractmethod
    def get_page(self, page_num):
        pass

    @abstractmethod
    def save_pdf(self, output_path):
        pass

    @abstractmethod
    def get_drawings(self, page_num):
        pass

    @abstractmethod
    def get_text(self, page_num, rect):
        pass

    @abstractmethod
    def draw_rectangle(self, page_num, rect, color):
        pass
