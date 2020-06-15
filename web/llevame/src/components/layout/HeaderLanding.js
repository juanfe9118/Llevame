import React from 'react';
import { Link } from 'react-router-dom';

function HeaderLanding() {
    return (
        <header style={headerStyle}>
            <h1 style={h1Style}>Llévame</h1>
            <div className='headerdiv'>
                <Link style={linkStyle} to='/login'>Log In</Link>
                <Link style={linkStyle} to='/signup'>Sign Up</Link>
            </div>
        </header>
    )
}

const headerStyle = {
    backgroundColor: '#29ABE2',
    color: '#fff',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between'
}

const h1Style = {
    marginLeft: '50px'
}

const linkStyle = {
    backgroundColor: '#fff',
    fontSize: '20px',
    border: '1px solid',
    borderRadius: '50px',
    padding: '5px 10px',
    margin: '0 10px',
}

export default HeaderLanding
