import React from 'react'
import { Link } from 'react-router-dom';

export default function Landing() {
    return (
        <div style={boxStyle}>
            <div style={leftDiv}>
                <h1 style={{fontSize: '50px'}}>Find people with similar destinations and chat with them</h1>
                <h3 style={{fontSize: '25px'}}>Sign up now and get started free!</h3><br></br>
                <Link style={linkStyle} to='/signup'>Sign Up</Link>
            </div>
            <div style={rightDiv}>
                <h1 style={{margin: '30px 0'}}>Chat</h1>
                <p style={recMes}>Hi...</p>
                <p style={senMes}>How are...</p>
                <p style={recMes}>Lorem ipsum....</p>
                <p style={senMes}>Lorem ipsum....</p>
                <div style={msgDiv}>
                    <p type="text" style={inputStyle}>Message</p>
                    <p style={btnStyle}>►</p>
                </div>
            </div>
        </div>
    )
}

const boxStyle = {
    height: '91vh',
    display: 'flex',
    justifyContent: 'space-evenly',
    alignItems: 'center',
}

const leftDiv = {
    height: '75%',
    width: '25%',
    display: 'flex',
    flexDirection: 'column',
    textAlign: 'center',
    alignItems: 'center',
    justifyContent: 'center',
}

const rightDiv = {
    height: '75%',
    width: '25%',
    alignItems: 'center',
    border: '#005DFF 1px solid',
    borderRadius: '15px',
    backgroundColor: '#29ABE2',
    display: 'flex',
    flexDirection: 'column',
}

const recMes = {
    width: '60%',
    margin: '8px 10px',
    padding: '10px',
    border: '#707070 1px solid',
    borderRadius: '15px',
    backgroundColor: '#fff',
    alignSelf: 'flex-start',
}

const senMes = {
    width: '60%',
    margin: '8px 10px',
    padding: '10px',
    border: '#707070 1px solid',
    borderRadius: '15px',
    backgroundColor: '#005DFF',
    opacity: '80%',
    alignSelf: 'flex-end',
}

const msgDiv = {
    margin: 'auto 0 25px',
    width: '100%',
    display: 'flex',
}

const inputStyle = {
    width: '70%',
    padding: '10px',
    margin: '0px 10px',
    backgroundColor: '#B3B3B3',
    color: '#fff',
    borderRadius: '15px',
}

const btnStyle = {
    margin: '0 10px',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    fontSize: '25px',
    width: '42px',
    height: '42px',
    borderRadius: '50%',
    backgroundColor: '#707070',
    color: '#005DFF',
    opacity: '80%',
}

const linkStyle = {
    backgroundColor: '#29ABE2', 
    color: '#fff',
    fontSize: '20px',
    border: '#707070 1px solid',
    borderRadius: '50px',
    padding: '5px 10px',
    margin: '0 10px',
}