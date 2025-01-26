// frontend/App.js
import React, { useEffect, useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet, Alert } from 'react-native';
import axios from 'axios';
import Geolocation from 'react-native-geolocation-service';
import { PermissionsAndroid, Platform } from 'react-native';

const App = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [latitude, setLatitude] = useState('');
    const [longitude, setLongitude] = useState('');

    useEffect(() => {
        requestLocationPermission();
    }, []);

    const requestLocationPermission = async () => {
        if (Platform.OS === 'android') {
            const granted = await PermissionsAndroid.request(
                PermissionsAndroid.PERMISSIONS.ACCESS_FINE_LOCATION,
                {
                    title: 'Location Permission',
                    message: 'This app needs access to your location.',
                    buttonNeutral: 'Ask Me Later',
                    buttonNegative: 'Cancel',
                    buttonPositive: 'OK',
                }
            );
            if (granted !== PermissionsAndroid.RESULTS.GRANTED) {
                Alert.alert('Location permission denied');
            }
        }
    };

    const getCurrentLocation = () => {
        Geolocation.getCurrentPosition(
            (position) => {
                const { latitude, longitude } = position.coords;
                setLatitude(latitude.toString());
                setLongitude(longitude.toString());
            },
            (error) => {
                Alert.alert('Error', 'Unable to retrieve location');
                console.error(error);
            },
            { enableHighAccuracy: true, timeout: 15000, maximumAge: 10000 }
        );
    };

    const registerUser  = async () => {
        try {
            const response = await axios.post('http://localhost:5000/register', { username, password });
            Alert.alert('Success', 'User  registered');
        } catch (error) {
            Alert.alert('Error', 'Failed to register user');
            console.error(error);
        }
    };

    const updateLocation = async () => {
        try {
            const response = await axios.post('http://localhost:5000/update-location', { username, latitude, longitude });
            Alert.alert('Success', 'Location updated');
        } catch (error) {
            Alert.alert('Error', 'Failed to update location');
            console.error(error);
        }
    };

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Register User</Text>
            <TextInput
                style={styles.input}
                placeholder="Username"
                value={username}
                onChangeText={setUsername}
            />
            <TextInput
                style={styles.input}
                placeholder="Password"
                secureTextEntry
                value={password}
                onChangeText={setPassword}
            />
            <Button title="Register" onPress={registerUser } />

            <Text style={styles.title}>Update Location</Text>
            <Button title="Get Current Location" onPress={getCurrentLocation} />
            <TextInput
                style={styles.input}
                placeholder="Latitude"
                value={latitude}
                editable={false}
            />
            <TextInput
                style={styles.input}
                placeholder="Longitude"
                value={longitude}
                editable={false}
            />
            <Button title="Update Location" onPress={updateLocation} />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        padding: 20,
        flex: 1,
        justifyContent: 'center',
    },
    title: {
        fontSize: 20,
        marginBottom: 10,
    },
    input: {
        height: 40,
        borderColor: 'gray',
        borderWidth: 1,
        marginBottom: 15,
        paddingHorizontal: 10,
    },
});

export default App;