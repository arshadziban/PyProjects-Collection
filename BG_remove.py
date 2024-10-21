from rembg import remove
from PIL import Image
from tkinter import Tk, Label, Button
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo

# Function to handle the background removal process
def remove_bg():
    #input file
    input_path = askopenfilename(title="Select an input image", filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    
    if input_path:
        # save the output file
        output_path = asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        
        if output_path:
            try:
                # Open the input image
                input_image = Image.open(input_path)
                
                # Remove the background
                output_image = remove(input_image)
                
                # Save the output image
                output_image.save(output_path)
                
                # Show success message
                showinfo("Success", f"Image saved successfully as {output_path}")
            except Exception as e:
                showinfo("Error", f"An error occurred: {e}")
        else:
            showinfo("Warning", "Output file not selected.")
    else:
        showinfo("Warning", "No image selected.")

#application window
root = Tk()
root.title("Background Remover")
root.geometry("300x150")  #window size


label = Label(root, text="Remove Image Background", font=("Arial", 14))
label.pack(pady=10)

# Button to trigger background removal
btn = Button(root, text="Select Image and Remove Background", command=remove_bg, font=("Arial", 10), padx=10, pady=5)
btn.pack(pady=20)

# Run 
root.mainloop()
