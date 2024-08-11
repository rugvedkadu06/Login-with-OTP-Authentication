// src/components/EmailInput.jsx

import React, { useState } from 'react';
import axios from 'axios';

function EmailInput() {
    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSendOTP = async () => {
        setLoading(true);
        try {
            const response = await axios.post('api-key-8lakgvj4a-rugvedkadu06s-projects.vercel.app/send-otp', { email });
            setMessage(response.data.message);
        } catch (error) {
            setMessage('Failed to send OTP. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ padding: '20px', maxWidth: '400px', margin: 'auto' }}>
            <h2>Request API</h2>
            <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Enter your email"
                style={{ width: '100%', padding: '10px', marginBottom: '10px' }}
            />
            <button
                onClick={handleSendOTP}
                disabled={loading}
                style={{ width: '100%', padding: '10px' }}
            >
                {loading ? 'Sending...' : 'Send OTP'}
            </button>
            {message && <p>{message}</p>}
        </div>
    );
}

export default EmailInput;
