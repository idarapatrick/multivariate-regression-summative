# Image Guide for Ubuntu Hypertension Prediction App

## 📁 Assets Folder Structure

Your assets folder is now set up at:
```
linear_regression_model/summative/FlutterApp/regression_app/assets/
├── images/
│   ├── icons/           # For small icons (heart, medical symbols, etc.)
│   ├── illustrations/   # For larger illustrations (doctors, charts, etc.)
│   └── [root images]    # For logos, backgrounds, etc.
└── README.md
```

## 🖼️ Where to Add Your Images

### 1. **Main Images** (assets/images/)
- `logo.png` - App logo with Ubuntu theme
- `background.jpg` - Background pattern
- `africa_map.png` - African continent map
- `app_icon.png` - App icon

### 2. **Icons** (assets/images/icons/)
- `heart_icon.png` - Heart health symbol
- `doctor_icon.png` - Medical professional icon
- `risk_low.png` - Low risk indicator
- `risk_moderate.png` - Moderate risk indicator
- `risk_high.png` - High risk indicator
- `risk_very_high.png` - Very high risk indicator
- `blood_pressure.png` - Blood pressure icon
- `africa_icon.png` - African continent icon

### 3. **Illustrations** (assets/images/illustrations/)
- `doctor_illustration.png` - Healthcare professional
- `patient_illustration.png` - Patient consultation
- `health_chart.png` - Health statistics chart
- `africa_health.png` - African healthcare scene

## 🎨 Recommended Image Specifications

### Logo & Icons
- **Format**: PNG (with transparency)
- **Size**: 512x512px (logo), 128x128px (icons)
- **Style**: Ubuntu orange (#E47B02) theme
- **Background**: Transparent

### Background Images
- **Format**: JPG or PNG
- **Size**: 1920x1080px or larger
- **Style**: Subtle, not distracting
- **Colors**: Warm tones, Ubuntu theme

### Illustrations
- **Format**: PNG or SVG
- **Size**: 800x600px or larger
- **Style**: Medical/healthcare themed
- **Colors**: Professional, accessible

## 💻 How to Use Images in Code

### Basic Image Usage
```dart
// Simple image
Image.asset('assets/images/logo.png')

// Image with size
Image.asset(
  'assets/images/icons/heart_icon.png',
  width: 50,
  height: 50,
)

// Image with fit
Image.asset(
  'assets/images/background.jpg',
  fit: BoxFit.cover,
)
```

### Image in Container
```dart
Container(
  width: 100,
  height: 100,
  decoration: BoxDecoration(
    image: DecorationImage(
      image: AssetImage('assets/images/background.jpg'),
      fit: BoxFit.cover,
    ),
  ),
)
```

### Image with Error Handling
```dart
Image.asset(
  'assets/images/logo.png',
  errorBuilder: (context, error, stackTrace) {
    return Icon(Icons.error, color: Colors.red);
  },
)
```

### Conditional Image Loading
```dart
Widget buildImage() {
  try {
    return Image.asset('assets/images/custom_icon.png');
  } catch (e) {
    return Icon(Icons.favorite, color: Color(0xFFE47B02));
  }
}
```

## 🔧 Integration Examples

### 1. Replace Heart Icon with Custom Image
```dart
// In main.dart, replace this:
Icon(Icons.favorite, size: 50, color: Colors.white)

// With this:
Image.asset(
  'assets/images/icons/heart_icon.png',
  width: 50,
  height: 50,
  color: Colors.white,
)
```

### 2. Add Background Image
```dart
Container(
  decoration: BoxDecoration(
    image: DecorationImage(
      image: AssetImage('assets/images/background.jpg'),
      fit: BoxFit.cover,
      opacity: 0.1, // Subtle background
    ),
  ),
  child: YourContent(),
)
```

### 3. Risk Level Icons
```dart
Widget getRiskIcon(String riskLevel) {
  switch (riskLevel) {
    case 'Low Risk':
      return Image.asset('assets/images/icons/risk_low.png', width: 30, height: 30);
    case 'Moderate Risk':
      return Image.asset('assets/images/icons/risk_moderate.png', width: 30, height: 30);
    case 'High Risk':
      return Image.asset('assets/images/icons/risk_high.png', width: 30, height: 30);
    case 'Very High Risk':
      return Image.asset('assets/images/icons/risk_very_high.png', width: 30, height: 30);
    default:
      return Icon(Icons.warning, color: Colors.orange);
  }
}
```

## 📱 Steps to Add Images

### Step 1: Prepare Your Images
1. Resize images to appropriate dimensions
2. Save in correct format (PNG for icons, JPG for photos)
3. Use descriptive names (lowercase with underscores)

### Step 2: Add to Assets Folder
1. Copy your images to the appropriate folder:
   - Icons → `assets/images/icons/`
   - Illustrations → `assets/images/illustrations/`
   - Main images → `assets/images/`

### Step 3: Update pubspec.yaml (Already Done)
The pubspec.yaml is already configured to include all images in `assets/images/`

### Step 4: Use in Code
1. Reference images using the path: `'assets/images/your_image.png'`
2. Test the app to ensure images load correctly

### Step 5: Test
1. Run `flutter pub get` to update dependencies
2. Hot restart the app to see changes
3. Test on different screen sizes

## 🎯 Specific Image Recommendations for This App

### Essential Images to Add:
1. **logo.png** - Ubuntu-themed app logo
2. **heart_icon.png** - Heart health symbol
3. **africa_map.png** - African continent outline
4. **doctor_icon.png** - Medical professional
5. **risk_indicators.png** - Risk level visual indicators

### Optional Enhancement Images:
1. **background_pattern.jpg** - Subtle background texture
2. **health_chart.png** - Medical statistics visualization
3. **patient_consultation.png** - Doctor-patient interaction
4. **blood_pressure_monitor.png** - Medical equipment

## 🚨 Troubleshooting

### Image Not Showing?
1. Check file path is correct
2. Ensure image is in the right folder
3. Run `flutter pub get`
4. Hot restart the app
5. Check file name case sensitivity

### Image Too Large/Small?
1. Use `width` and `height` parameters
2. Use `fit: BoxFit.contain` or `BoxFit.cover`
3. Wrap in `Container` with specific dimensions

### Performance Issues?
1. Compress images (keep under 1MB)
2. Use appropriate formats (PNG for icons, JPG for photos)
3. Consider using `precacheImage()` for frequently used images

## 📝 Next Steps

1. **Add your custom images** to the appropriate folders
2. **Update the code** to use your images instead of icons
3. **Test the app** to ensure everything works
4. **Optimize images** for performance if needed

Your assets folder is now ready! Just add your images and start using them in the app. 🎉 