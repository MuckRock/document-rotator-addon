"""
This Add-On detects the orientation of text on a page 
in a document and rotates the pages accordingly by detecting 
a skew angle using an approximation. It saves the modified
document and uploads it as a new document, preserving the
original. 
"""
import os
from documentcloud.addon import AddOn
from rotate import skew_correction, main as skew_correction_main

class Rotator(AddOn):

    def main(self):
        """The main add-on functionality goes here."""
        self.set_message("Starting Document Rotator")
        os.makedirs(os.path.dirname("./out/"), exist_ok=True)
        for document in self.get_documents():
            title = document.title
            with open(f"{title}.pdf", "wb") as file:
                file.write(document.pdf)
            skew_correction_main(f"{title}.pdf", f"./out/{title}_rotated.pdf")
        self.client.documents.upload_directory("./out/")


if __name__ == "__main__":
    Rotator().main()
