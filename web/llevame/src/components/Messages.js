import React, { Component } from 'react';
import axios from 'axios';
import Message from './Message';

export class Messages extends Component {
    state = {
        message: ''
    }

    sendMsg = (e) => {
        e.preventDefault();
        const headers = {
            Authorization: 'Token ' + this.props.token
        }
        axios.post('http://localhost:8000/api/messages/', {
            user: this.props.user_id,
            chat: this.props.chat,
            content: this.state.message
        }, {headers: headers})
            .then(res => {
                this.props.loadChat();
            })
            .catch(err => console.log(err.response.data));
            this.setState({message: ''});
        
    }

    onChange = (e) => this.setState({ [e.target.name]: e.target.value });

    render() {
        return (
            <div style={rightDiv}>
                <Message messages={this.props.messages} user_id={this.props.user_id} />
                <form style={msgDiv} onSubmit={this.sendMsg}>
                    <input style={inputStyle} type='text' placeholder='Message' name='message' onChange={this.onChange} value={this.state.message} />
                    <input style={btnStyle} type='submit' value='►' />
                </form>
            </div>
        )
    }
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

export default Messages
