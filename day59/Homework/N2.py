def create_paragraph():
    text = input("Enter text: ")
    color = input("Enter text color: ")
    bg_color = input("Enter background color: ")
    paragraph = f"<p style='color: {color}; background-color: {bg_color};'>{text}</p>"
    print(paragraph)

create_paragraph()
