import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(UbuntuHypertensionApp());
}

class UbuntuHypertensionApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Ubuntu Hypertension Prediction',
      theme: ThemeData(
        primarySwatch: Colors.orange,
        primaryColor: Color(0xFFE47B02), // Ubuntu Orange
        scaffoldBackgroundColor: Color(0xFFF7F5F3), // Warm off-white
        colorScheme: ColorScheme.fromSeed(
          seedColor: Color(0xFFE47B02),
          brightness: Brightness.light,
        ),
        fontFamily: 'Ubuntu',
        textTheme: TextTheme(
          headlineLarge: TextStyle(
            color: Color(0xFF2C2C2C),
            fontWeight: FontWeight.bold,
            fontSize: 28,
          ),
          headlineMedium: TextStyle(
            color: Color(0xFF4A4A4A),
            fontWeight: FontWeight.w600,
            fontSize: 24,
          ),
          bodyLarge: TextStyle(
            color: Color(0xFF2C2C2C),
            fontSize: 16,
          ),
          bodyMedium: TextStyle(
            color: Color(0xFF4A4A4A),
            fontSize: 14,
          ),
        ),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            backgroundColor: Color(0xFFE47B02),
            foregroundColor: Colors.white,
            padding: EdgeInsets.symmetric(horizontal: 32, vertical: 16),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(12),
            ),
            elevation: 4,
          ),
        ),
        inputDecorationTheme: InputDecorationTheme(
          filled: true,
          fillColor: Colors.white,
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(12),
            borderSide: BorderSide(color: Color(0xFFE0E0E0)),
          ),
          focusedBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(12),
            borderSide: BorderSide(color: Color(0xFFE47B02), width: 2),
          ),
          enabledBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(12),
            borderSide: BorderSide(color: Color(0xFFE0E0E0)),
          ),
          contentPadding: EdgeInsets.symmetric(horizontal: 16, vertical: 16),
        ),
      ),
      home: SplashScreen(),
      routes: {
        '/home': (context) => HomePage(),
        '/prediction': (context) => PredictionPage(),
      },
    );
  }
}

class SplashScreen extends StatefulWidget {
  @override
  _SplashScreenState createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen>
    with SingleTickerProviderStateMixin {
  late AnimationController _animationController;
  late Animation<double> _fadeAnimation;

  @override
  void initState() {
    super.initState();
    _animationController = AnimationController(
      duration: Duration(seconds: 2),
      vsync: this,
    );
    _fadeAnimation = Tween<double>(begin: 0.0, end: 1.0).animate(
      CurvedAnimation(parent: _animationController, curve: Curves.easeIn),
    );

    _animationController.forward();

    Future.delayed(Duration(seconds: 3), () {
      Navigator.pushReplacementNamed(context, '/home');
    });
  }

  @override
  void dispose() {
    _animationController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xFFE47B02),
      body: FadeTransition(
        opacity: _fadeAnimation,
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                width: 120,
                height: 120,
                decoration: BoxDecoration(
                  color: Colors.white,
                  shape: BoxShape.circle,
                  boxShadow: [
                    BoxShadow(
                      color: Colors.black.withOpacity(0.2),
                      blurRadius: 10,
                      offset: Offset(0, 5),
                    ),
                  ],
                ),
                child: Center(
                  child: Icon(
                    Icons.favorite,
                    size: 60,
                    color: Color(0xFFE47B02),
                  ),
                ),
              ),
              SizedBox(height: 24),
              Text(
                'Ubuntu',
                style: TextStyle(
                  fontSize: 36,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
              Text(
                'Hypertension Prediction',
                style: TextStyle(
                  fontSize: 18,
                  color: Colors.white.withOpacity(0.9),
                ),
              ),
              SizedBox(height: 40),
              CircularProgressIndicator(
                valueColor: AlwaysStoppedAnimation<Color>(Colors.white),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: SingleChildScrollView(
          child: Padding(
            padding: EdgeInsets.all(24.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                SizedBox(height: 20),
                Center(
                  child: Column(
                    children: [
                      Container(
                        width: 100,
                        height: 100,
                        decoration: BoxDecoration(
                          gradient: LinearGradient(
                            colors: [Color(0xFFE47B02), Color(0xFFFF8C42)],
                            begin: Alignment.topLeft,
                            end: Alignment.bottomRight,
                          ),
                          shape: BoxShape.circle,
                          boxShadow: [
                            BoxShadow(
                              color: Color(0xFFE47B02).withOpacity(0.3),
                              blurRadius: 20,
                              offset: Offset(0, 10),
                            ),
                          ],
                        ),
                        child: Icon(
                          Icons.favorite,
                          size: 50,
                          color: Colors.white,
                        ),
                        // Alternative: Use custom image
                        // child: Image.asset(
                        //   'assets/images/icons/heart_icon.png',
                        //   width: 50,
                        //   height: 50,
                        //   color: Colors.white,
                        // ),
                      ),
                      SizedBox(height: 16),
                      Text(
                        'Ubuntu',
                        style: Theme.of(context).textTheme.headlineLarge,
                      ),
                      Text(
                        'Hypertension Prediction',
                        style: Theme.of(context).textTheme.headlineMedium?.copyWith(
                          color: Color(0xFFE47B02),
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                      SizedBox(height: 8),
                      Text(
                        '"Built by an African for Africans"',
                        style: TextStyle(
                          fontSize: 14,
                          fontStyle: FontStyle.italic,
                          color: Color(0xFF666666),
                        ),
                      ),
                    ],
                  ),
                ),
                SizedBox(height: 40),
                Container(
                  padding: EdgeInsets.all(20),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(16),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black.withOpacity(0.1),
                        blurRadius: 10,
                        offset: Offset(0, 5),
                      ),
                    ],
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        children: [
                          Icon(
                            Icons.info_outline,
                            color: Color(0xFFE47B02),
                            size: 24,
                          ),
                          SizedBox(width: 8),
                          Text(
                            'About Ubuntu Philosophy',
                            style: TextStyle(
                              fontSize: 18,
                              fontWeight: FontWeight.bold,
                              color: Color(0xFF2C2C2C),
                            ),
                          ),
                        ],
                      ),
                      SizedBox(height: 12),
                      Text(
                        'Ubuntu is an African philosophy meaning "humanity". It emphasizes the interconnectedness of all people. "I am because we are". This app embodies that spirit by providing healthcare insights to strengthen our African community.',
                        style: TextStyle(
                          fontSize: 14,
                          color: Color(0xFF4A4A4A),
                          height: 1.5,
                        ),
                      ),
                    ],
                  ),
                ),
                SizedBox(height: 24),
                Container(
                  padding: EdgeInsets.all(20),
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      colors: [Color(0xFFFFF3E0), Color(0xFFFFE0B2)],
                      begin: Alignment.topLeft,
                      end: Alignment.bottomRight,
                    ),
                    borderRadius: BorderRadius.circular(16),
                    border: Border.all(
                      color: Color(0xFFE47B02).withOpacity(0.3),
                      width: 1,
                    ),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        children: [
                          Icon(
                            Icons.health_and_safety,
                            color: Color(0xFFE47B02),
                            size: 24,
                          ),
                          SizedBox(width: 8),
                          Text(
                            'Hypertension Risk Assessment',
                            style: TextStyle(
                              fontSize: 18,
                              fontWeight: FontWeight.bold,
                              color: Color(0xFF2C2C2C),
                            ),
                          ),
                        ],
                      ),
                      SizedBox(height: 12),
                      Text(
                        'Get personalized hypertension risk predictions based on your age, gender, and country. Our AI model uses data from across African nations to provide accurate assessments.',
                        style: TextStyle(
                          fontSize: 14,
                          color: Color(0xFF4A4A4A),
                          height: 1.5,
                        ),
                      ),
                      SizedBox(height: 16),
                      Row(
                        children: [
                          _buildRiskIndicator('🟢', 'Low', '0-25%'),
                          SizedBox(width: 12),
                          _buildRiskIndicator('🟡', 'Moderate', '25-40%'),
                          SizedBox(width: 12),
                          _buildRiskIndicator('🟠', 'High', '40-60%'),
                          SizedBox(width: 12),
                          _buildRiskIndicator('🔴', 'Very High', '60%+'),
                        ],
                      ),
                    ],
                  ),
                ),
                SizedBox(height: 32),
                Center(
                  child: ElevatedButton(
                    onPressed: () {
                      Navigator.pushNamed(context, '/prediction');
                    },
                    style: ElevatedButton.styleFrom(
                      padding: EdgeInsets.symmetric(horizontal: 48, vertical: 20),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(16),
                      ),
                    ),
                    child: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Icon(Icons.health_and_safety, size: 24),
                        SizedBox(width: 8),
                        Text(
                          'Start Prediction',
                          style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                  ),
                ),
                SizedBox(height: 24),
                Center(
                  child: Text(
                    '🌍 Proudly African 🌍',
                    style: TextStyle(
                      fontSize: 16,
                      color: Color(0xFF666666),
                      fontWeight: FontWeight.w500,
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildRiskIndicator(String emoji, String label, String range) {
    return Expanded(
      child: Container(
        padding: EdgeInsets.symmetric(vertical: 8, horizontal: 4),
        decoration: BoxDecoration(
          color: Colors.white.withOpacity(0.7),
          borderRadius: BorderRadius.circular(8),
        ),
        child: Column(
          children: [
            Text(emoji, style: TextStyle(fontSize: 16)),
            SizedBox(height: 2),
            Text(
              label,
              style: TextStyle(
                fontSize: 10,
                fontWeight: FontWeight.bold,
                color: Color(0xFF2C2C2C),
              ),
            ),
            Text(
              range,
              style: TextStyle(
                fontSize: 8,
                color: Color(0xFF666666),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class PredictionPage extends StatefulWidget {
  @override
  _PredictionPageState createState() => _PredictionPageState();
}

class _PredictionPageState extends State<PredictionPage> {
  final _formKey = GlobalKey<FormState>();
  final _nameController = TextEditingController();
  final _ageController = TextEditingController();
  String? _selectedSex;
  String? _selectedCountry;
  String _result = '';
  bool _isLoading = false;

  final List<String> _sexOptions = ['Men', 'Women'];
  final List<String> _africanCountries = [
    'Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi',
    'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros',
    'Democratic Republic of the Congo', 'Republic of the Congo', 'Côte d\'Ivoire',
    'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia',
    'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho',
    'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius',
    'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda',
    'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia',
    'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia',
    'Uganda', 'Zambia', 'Zimbabwe'
  ];

  Future<void> _makePrediction() async {
    if (!_formKey.currentState!.validate()) return;

    setState(() {
      _isLoading = true;
      _result = '';
    });

    try {
      // Prepare request data
      final requestData = {
        'age': int.parse(_ageController.text),
        'sex': _selectedSex ?? 'Women', // Provide default if null
        'year': 2024, // Current year
        'country': _selectedCountry ?? 'Nigeria', // Provide default if null
      };
      
      // Debug: Print what we're sending
      print('Sending to API: ${jsonEncode(requestData)}');
      
      // Replace with your actual Railway API endpoint
      final response = await http.post(
        Uri.parse('https://prediction-api.up.railway.app/predict'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode(requestData),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        final prediction = data['prediction'] ?? 0.0;
        final ageGroup = data['age_group'] ?? '';
        final message = data['message'] ?? '';
        final modelUsed = data['model_used'] ?? 'AI Model';
        _displayResult(prediction, ageGroup, message, modelUsed);
      } else {
        final errorData = jsonDecode(response.body);
        print('API Error Response: ${response.body}');
        String errorMessage = 'Unable to get prediction. Please try again.';
        
        // Handle validation errors
        if (errorData['detail'] is List) {
          for (var error in errorData['detail']) {
            print('Validation Error: $error');
            if (error['loc'] != null && error['loc'].contains('sex')) {
              errorMessage = 'Error: Sex must be "Men" or "Women". Please check your selection.';
              break;
            } else if (error['loc'] != null && error['loc'].contains('country')) {
              errorMessage = 'Error: Please select a valid African country.';
              break;
            } else if (error['loc'] != null && error['loc'].contains('age')) {
              errorMessage = 'Error: Age must be between 30 and 100 years.';
              break;
            }
          }
        } else if (errorData['detail'] is String) {
          errorMessage = 'Error: ${errorData['detail']}';
        }
        
        setState(() {
          _result = errorMessage;
        });
      }
    } catch (e) {
      // Fallback to simulated prediction if API is not available
      print('API Error: $e');
      await Future.delayed(const Duration(seconds: 1)); // Simulate API call
      
      // Simulate a prediction result for demo purposes
      double simulatedPrediction = 0.35; // 35% - Moderate Risk
      String simulatedAgeGroup = '45-49';
      String simulatedMessage = 'Based on your demographic profile (age: 45, sex: Women, country: Nigeria)';
      String simulatedModel = 'Simulated Model';
      
      _displayResult(simulatedPrediction, simulatedAgeGroup, simulatedMessage, simulatedModel);
    } finally {
      setState(() {
        _isLoading = false;
      });
    }
  }

  void _displayResult(double prediction, String ageGroup, String message, String modelUsed) {
    String riskLevel;
    String emoji;
    String advice;
    Color riskColor;

    if (prediction <= 0.25) {
      riskLevel = 'Low Risk';
      emoji = '🟢';
      advice = 'Normal range. Continue healthy lifestyle.';
      riskColor = Colors.green;
    } else if (prediction <= 0.40) {
      riskLevel = 'Moderate Risk';
      emoji = '🟡';
      advice = 'Moderate risk. Consider lifestyle changes and monitor blood pressure.';
      riskColor = Colors.orange;
    } else if (prediction <= 0.60) {
      riskLevel = 'High Risk';
      emoji = '🟠';
      advice = 'High risk. Consult a healthcare provider for evaluation.';
      riskColor = Colors.deepOrange;
    } else {
      riskLevel = 'Very High Risk';
      emoji = '🔴';
      advice = 'Very high risk. Seek immediate medical attention.';
      riskColor = Colors.red;
    }

    setState(() {
      _result = '''Hi, ${_nameController.text}! 

${emoji} **HYPER TENSION RISK ASSESSMENT** ${emoji}

**Prevalence:** ${(prediction * 100).toStringAsFixed(1)}%
**Risk Level:** $riskLevel
**Age Group:** $ageGroup

**Health Advice:**
$advice

**Additional Information:**
$message

**Model Used:** $modelUsed

This prediction is based on your demographic profile (age: ${_ageController.text}, sex: $_selectedSex, country: $_selectedCountry).

${prediction == 0.35 ? 'Note: This is a simulated result for demo purposes.' : ''}''';
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Hypertension Prediction'),
        backgroundColor: Color(0xFFE47B02),
        foregroundColor: Colors.white,
        elevation: 0,
      ),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: EdgeInsets.all(24.0),
          child: Form(
            key: _formKey,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                Container(
                  padding: EdgeInsets.all(20),
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      colors: [Color(0xFFE47B02), Color(0xFFFF8C42)],
                      begin: Alignment.topLeft,
                      end: Alignment.bottomRight,
                    ),
                    borderRadius: BorderRadius.circular(16),
                  ),
                  child: Column(
                    children: [
                      Icon(
                        Icons.health_and_safety,
                        size: 48,
                        color: Colors.white,
                      ),
                      SizedBox(height: 12),
                      Text(
                        'Health Assessment',
                        style: TextStyle(
                          fontSize: 24,
                          fontWeight: FontWeight.bold,
                          color: Colors.white,
                        ),
                      ),
                      Text(
                        'Enter your details for personalized prediction',
                        style: TextStyle(
                          fontSize: 14,
                          color: Colors.white.withOpacity(0.9),
                        ),
                      ),
                    ],
                  ),
                ),
                SizedBox(height: 32),
                
                // Name Field
                TextFormField(
                  controller: _nameController,
                  decoration: InputDecoration(
                    labelText: 'Your Name',
                    prefixIcon: Icon(Icons.person, color: Color(0xFFE47B02)),
                    hintText: 'Enter your full name',
                  ),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please enter your name';
                    }
                    return null;
                  },
                ),
                SizedBox(height: 20),
                
                // Age Field
                TextFormField(
                  controller: _ageController,
                  decoration: InputDecoration(
                    labelText: 'Age',
                    prefixIcon: Icon(Icons.cake, color: Color(0xFFE47B02)),
                    hintText: 'Enter your age (30-100)',
                  ),
                  keyboardType: TextInputType.number,
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please enter your age';
                    }
                    final age = int.tryParse(value);
                    if (age == null || age < 30 || age > 90) {
                      return 'Please enter a valid age (30-90)';
                    }
                    return null;
                  },
                ),
                SizedBox(height: 20),
                
                // Sex Dropdown
                DropdownButtonFormField<String>(
                  value: _selectedSex,
                  decoration: InputDecoration(
                    labelText: 'Sex',
                    prefixIcon: Icon(Icons.people, color: Color(0xFFE47B02)),
                  ),
                  items: _sexOptions.map((String sex) {
                    return DropdownMenuItem<String>(
                      value: sex,
                      child: Text(sex),
                    );
                  }).toList(),
                  onChanged: (String? newValue) {
                    setState(() {
                      _selectedSex = newValue;
                    });
                  },
                  validator: (value) {
                    if (value == null) {
                      return 'Please select your sex';
                    }
                    return null;
                  },
                ),
                SizedBox(height: 20),
                
                // Country Dropdown
                DropdownButtonFormField<String>(
                  value: _selectedCountry,
                  decoration: InputDecoration(
                    labelText: 'Country',
                    prefixIcon: Icon(Icons.public, color: Color(0xFFE47B02)),
                  ),
                  items: _africanCountries.map((String country) {
                    return DropdownMenuItem<String>(
                      value: country,
                      child: Text(country),
                    );
                  }).toList(),
                  onChanged: (String? newValue) {
                    setState(() {
                      _selectedCountry = newValue;
                    });
                  },
                  validator: (value) {
                    if (value == null) {
                      return 'Please select your country';
                    }
                    return null;
                  },
                ),
                SizedBox(height: 32),
                
                // Predict Button
                ElevatedButton(
                  onPressed: _isLoading ? null : _makePrediction,
                  style: ElevatedButton.styleFrom(
                    padding: EdgeInsets.symmetric(vertical: 20),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(16),
                    ),
                  ),
                  child: _isLoading
                      ? CircularProgressIndicator(color: Colors.white)
                      : Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Icon(Icons.analytics, size: 24),
                            SizedBox(width: 8),
                            Text(
                              'Predict',
                              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                            ),
                          ],
                        ),
                ),
                SizedBox(height: 24),
                
                // Results Display
                if (_result.isNotEmpty)
                  Container(
                    padding: EdgeInsets.all(20),
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(16),
                      border: Border.all(
                        color: Color(0xFFE47B02).withOpacity(0.3),
                        width: 2,
                      ),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withOpacity(0.1),
                          blurRadius: 10,
                          offset: Offset(0, 5),
                        ),
                      ],
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          children: [
                            Icon(
                              Icons.assessment,
                              color: Color(0xFFE47B02),
                              size: 24,
                            ),
                            SizedBox(width: 8),
                            Text(
                              'Prediction Result',
                              style: TextStyle(
                                fontSize: 18,
                                fontWeight: FontWeight.bold,
                                color: Color(0xFF2C2C2C),
                              ),
                            ),
                          ],
                        ),
                        SizedBox(height: 16),
                        Text(
                          _result,
                          style: TextStyle(
                            fontSize: 16,
                            color: Color(0xFF2C2C2C),
                            height: 1.5,
                          ),
                        ),
                      ],
                    ),
                  ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  @override
  void dispose() {
    _nameController.dispose();
    _ageController.dispose();
    super.dispose();
  }
}