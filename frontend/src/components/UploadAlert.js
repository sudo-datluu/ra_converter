import React, { useEffect } from 'react';
import { Alert } from 'react-bootstrap';

const UploadAlert = ({ show, message, variant = "success", onClose }) => {
    useEffect(() => {
        if (show) {
            const timer = setTimeout(() => {
                onClose(); // Call the onClose function to hide the alert
            }, 5000); // 5000 milliseconds = 5 seconds

            return () => clearTimeout(timer); // Clear the timer if the component unmounts
        }
    }, [show, onClose]);

    if (!show) return null;

    return (
        <Alert 
            variant={variant} 
            onClose={onClose} 
            dismissible 
            style={{
                position: 'fixed', 
                top: '20px', 
                right: '20px', 
                zIndex: 9999
            }}>
            {message}
        </Alert>
    );
};

export default UploadAlert;
