import React, { Component } from 'react'

export class LoadMessage extends Component {
    render() {
        return (
            <p style={(this.props.user_id === this.props.message.user) ? senMes : recMes} >{this.props.message.content}</p>
        )
    }
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

export default LoadMessage
