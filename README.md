# 🎨 Divine Ganesha Drawing with MUSIC
<img width="1299" height="973" alt="image" src="https://github.com/user-attachments/assets/b957e947-8735-417d-9f51-8d581e267541" />

A beautiful Python application that creates an animated Lord Ganesha drawing with Sanskrit prayers, background music, and falling flowers effect - perfect for Ganesh Chaturthi celebrations.

## 🙏 Features

### ✨ **DrawingGanapatiUsingPython.py**
- **Animated Ganapati Drawing**: Step-by-step creation of Lord Ganesha using Turtle graphics
- **Sanskrit Prayer Display**: Real-time console output of sacred verses during drawing
- **Background Music**: Continuous devotional music playback
- **Falling Flowers Effect**: Continuous shower of colorful flowers falling over the image
- **Large Prayer Text**: 22pt bold Sanskrit text displayed beside the drawing
- **No Border Lines**: Clean, distraction-free presentation
- **Multi-threaded**: Music and flowers run simultaneously

### 🖥️ **Sanskrit_Prayer_GUI.py**
- **Beautiful GUI Interface**: Professional devotional design with dark brown theme
- **Sanskrit Prayer Display**: Large, readable Devanagari text
- **English Translation**: Complete meaning explanation
- **Background Music**: Integrated audio playback
- **Responsive Design**: Centered window with proper spacing
- **Easy Controls**: Simple close button interface

## 📋 Requirements

### System Requirements
- **Python**: 3.7 or higher
- **Operating System**: Windows 10/11, macOS, or Linux
- **RAM**: Minimum 2GB
- **Storage**: 100MB free space

### Python Libraries
```
pygame>=2.0.0
tkinter (built-in with Python)
turtle (built-in with Python)
threading (built-in with Python)
random (built-in with Python)
time (built-in with Python)
```

## 🚀 Installation

### Step 1: Install Python
1. Download Python from [python.org](https://python.org)
2. Run the installer
3. Make sure to check "Add Python to PATH" during installation
4. Verify installation: `python --version`

### Step 2: Install Required Libraries
Open Command Prompt/Terminal and run:
```bash
pip install pygame
```

### Step 3: Download Music File (Optional)
The application looks for a music file at:
```
C:\Users\[YourUsername]\Pictures\Danka Baja - RaagJatt.mp3
```

**To add your own music:**
1. Place any MP3 file in your Pictures folder
2. Rename it to `Danka Baja - RaagJatt.mp3`
3. Or modify the file path in the code

## 🎯 Usage

### Running the Animated Drawing
```bash
cd path/to/your/files
python DrawingGanapatiUsingPython.py
```

**What you'll see:**
1. Console displays Sanskrit prayer as drawing progresses
2. Turtle window opens with animated Ganapati creation
3. Background music starts playing
4. Falling flowers begin after drawing completes
5. Sanskrit prayer appears beside the final image

### Running the GUI Prayer App
```bash
cd path/to/your/files
python Sanskrit_Prayer_GUI.py
```

**Features:**
- Beautiful GUI window with prayer display
- English translation included
- Background music integration
- Centered on screen automatically

## 📁 File Structure

```
Ganapati_Project/
├── DrawingGanapatiUsingPython.py    # Main animated drawing application
├── Sanskrit_Prayer_GUI.py          # GUI prayer display application
├── README.md                       # This documentation file
└── Pictures/                       # (Optional) Music file location
    └── Danka Baja - RaagJatt.mp3
```

## 🎨 Application Details

### DrawingGanapatiUsingPython.py Features:
- **Drawing Stages**: Head → Face → Eyes → Ears → Trunk → Decorations → Text
- **Prayer Integration**: Sanskrit verses appear in console during each stage
- **Flower Animation**: 7 different colors, random sizes and positions
- **Audio**: Continuous loop playback
- **Error Handling**: Graceful handling of missing music files

### Sanskrit_Prayer_GUI.py Features:
- **Responsive Layout**: Adapts to different screen sizes
- **Color Scheme**: Traditional devotional colors (gold, brown, red)
- **Typography**: Multiple font sizes for hierarchy
- **Accessibility**: Clear text with good contrast

## 🔧 Customization

### Changing Music File
Edit the music path in both files:
```python
pygame.mixer.music.load(r"C:\Users\prana\Pictures\YourMusicFile.mp3")
```

### Modifying Colors
Update the color schemes in the respective files:
```python
# For drawing colors
t.color("gold")  # Change to any color

# For flower colors
colors = ["red", "pink", "blue", "purple"]  # Add/remove colors
```

### Adjusting Text Size
Modify font sizes:
```python
# For drawing text
t.write(text, font=("arial", 22, "bold"))  # Change 22 to desired size

# For GUI text
prayer_font = font.Font(family="Arial Unicode MS", size=18, weight="bold")
```

## 🐛 Troubleshooting

### Common Issues:

**1. "Module 'pygame' not found"**
```bash
pip install pygame
```

**2. "No music file found"**
- Place MP3 file in Pictures folder
- Or modify the file path in code
- Or comment out music lines for silent operation

**3. "Turtle graphics not responding"**
- Close any existing turtle windows
- Restart the application
- Check for multiple running instances

**4. "Unicode text not displaying correctly"**
- Ensure you have Unicode fonts installed
- Try different font families: "Arial Unicode MS", "Mangal", "Nirmala UI"

**5. "Window not centering properly"**
- The GUI automatically centers itself
- For manual positioning, modify the `center_window()` function

### Performance Tips:
- Close other applications for better performance
- Ensure sufficient RAM (2GB minimum)
- Use SSD for faster loading

## 📝 Sanskrit Prayer

The application features the sacred Ganesh prayer:

**वक्रतुंड महाकाय सूर्यकोटि समप्रभ।**  
**निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा॥**

**English Translation:**  
"O Lord Ganesha with curved trunk and massive body, brilliant as a million suns, please make all my endeavors free from obstacles, always and forever."

## 🤝 Contributing

Feel free to:
- Add more prayers
- Improve the drawing design
- Add more animation effects
- Enhance the GUI design
- Add more language translations

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Created for Ganesh Chaturthi celebrations
- Inspired by traditional Indian art and spirituality
- Uses Python's Turtle graphics for educational purposes
---
**🎉 Happy Ganesh Chaturthi! May Lord Ganesha bless you with wisdom and remove all obstacles from your path. 🙏**
