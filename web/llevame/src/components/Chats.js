import React, { Component } from 'react'
import {Redirect} from 'react-router-dom';
import axios from 'axios';
import Chat from './Chat';

export class Chats extends Component {
    state = {
        chats: [],
        redirect: null,
    }
    loadChat = () => {
        const headers = {
            Authorization: 'Token ' + this.props.token
        }
        axios.get('http://localhost:8000/api/chats/', {headers: headers})
            .then(res => {
                this.setState({chats: res.data.results})
            })
            .catch(err => console.log(err.response.data));


        /*axios.post('http://localhost:8000/api/chats/', {
            users: [2, 3],       
        }, {headers: headers})
            .then(res => console.log(res.data))
            .catch(err => console.log(err.response.data));*/
    }

    render() {
        if (this.state.redirect) {
            return <Redirect to={this.state.redirect} />
          }
        return (
            <div>
                <button onClick={this.loadChat}>Load Chat</button>
                <Chat chats={this.state.chats} loadChat={this.loadChat.bind(this)} token={this.props.token} user_id={this.props.user_id} />
            </div>
        )
    }
}

export default Chats
