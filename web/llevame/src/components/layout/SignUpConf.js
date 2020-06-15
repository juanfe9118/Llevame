import React from 'react';
import { Link } from 'react-router-dom';

export default function SignUpConf() {
    return (
        <div>
            <p>User created successfully please </p>
            <Link to='/login'>sign in.</Link>
        </div>
    )
}
