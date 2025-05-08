import 'package:flutter/material.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import '../../services/auth_service.dart';

class LoginScreen extends StatefulWidget {
  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _formKey = GlobalKey<FormState>();
  final _authService = AuthService();
  final _storage = FlutterSecureStorage();
  String _username = '';
  String _password = '';

  Future<void> _login() async {
    if (_formKey.currentState!.validate()) {
      try {
        final token = await _authService.login(_username, _password);
        await _storage.write(key: 'token', value: token);
        Navigator.pushReplacementNamed(context, '/dashboard');
      } catch (e) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Login failed: $e')),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(title: Text('Login')),
    body: Padding(
    padding: EdgeInsets.all(16.0),
    child: Form(
    key: _formKey,
    child: Column(
    children: [
    TextFormField(
    decoration: InputDecoration(labelText: 'Username'),
    validator: (value) => value!.isEmpty ? 'Required' : null,
    onChanged: (value) => _username = value,
    ),
    TextFormField(
    decoration: InputDecoration(labelText: 'Password'),
    obscureText: true,
    validator: (value) => value!.isEmpty ? 'Required' : null,
    onChanged: (value) => _password = value,
    ),
    ElevatedButton(
    onPressed: _login,
    child: Text('Login'),
    ),
    ],
