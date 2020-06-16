import React from 'react'

export default function UserHeader() {
    return (
        <header style={headerStyle}>
            <h1 style={h1Style}>Llévame</h1>
            
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
