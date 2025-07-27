# Assets Folder

This folder contains all the static assets for the Ubuntu Hypertension Prediction App.

## Folder Structure

```
assets/
├── images/          # All image files (PNG, JPG, SVG, etc.)
│   ├── logo.png     # App logo
│   ├── background.jpg # Background images
│   ├── icons/       # Icon images
│   └── illustrations/ # Illustration images
├── fonts/           # Custom fonts (if needed)
└── README.md        # This file
```

## Supported Image Formats

- **PNG** - Best for logos, icons, and images with transparency
- **JPG/JPEG** - Best for photographs and complex images
- **SVG** - Vector graphics (scalable)
- **WebP** - Modern format with good compression

## How to Use Images in Flutter

### 1. Add Images to the Folder
Place your image files in the `assets/images/` folder.

### 2. Reference in Code
```dart
// For images in assets/images/
Image.asset('assets/images/logo.png')

// For images in subfolders
Image.asset('assets/images/icons/heart.png')
```

### 3. Common Image Widgets
```dart
// Basic image
Image.asset('assets/images/logo.png')

// Image with specific size
Image.asset(
  'assets/images/logo.png',
  width: 100,
  height: 100,
)

// Image with fit
Image.asset(
  'assets/images/background.jpg',
  fit: BoxFit.cover,
)

// Image in a container
Container(
  decoration: BoxDecoration(
    image: DecorationImage(
      image: AssetImage('assets/images/background.jpg'),
      fit: BoxFit.cover,
    ),
  ),
)
```

## Recommended Images for This App

1. **logo.png** - Ubuntu-themed app logo
2. **heart_icon.png** - Heart health icon
3. **africa_map.png** - African continent map
4. **doctor.png** - Healthcare professional illustration
5. **background.jpg** - Subtle background pattern
6. **risk_low.png** - Low risk indicator
7. **risk_moderate.png** - Moderate risk indicator
8. **risk_high.png** - High risk indicator
9. **risk_very_high.png** - Very high risk indicator

## Image Guidelines

- **Size**: Keep images under 1MB when possible
- **Resolution**: Use appropriate resolution (2x for high-DPI displays)
- **Format**: Use PNG for icons/logos, JPG for photos
- **Naming**: Use lowercase with underscores (e.g., `heart_icon.png`)

## After Adding Images

1. Add images to the `assets/images/` folder
2. Run `flutter pub get` to update dependencies
3. Hot restart the app to see changes 