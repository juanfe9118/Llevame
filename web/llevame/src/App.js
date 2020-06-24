import React, { Component } from 'react';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import { Redirect } from 'react-router-dom';
import axios from 'axios';

import HeaderLanding from './components/layout/HeaderLanding';
import Footer from './components/layout/Footer';
import Landing from './components/layout/Landing';
import FormHeader from './components/layout/FormHeader';
import SignUp from './components/SignUp';
import LogIn from './components/LogIn';
import SignUpConf from './components/layout/SignUpConf';
import UserHeader from './components/layout/UserHeader';
import UserLanding from './components/UserLanding';
import Chats from './components/Chats';

import VehicleRegister from './components/Vehicle';

import './App.css';

class App extends Component {
  state = {
    email: '',
    password: '',
    token: null,
    user_id: null,
    redirect: '/',
    user_info: {},
  }

  componentDidMount() {
    if (this.state.token) {
      this.setState({ redirect: './userlanding' });
    }
  }

  signOut = () => {
    this.setState({token: null});
    this.setState({user_id: null});
    this.setState({user_info: null});
    this.setState({redirect: '/'});
  };

  onChange = (e) => this.setState({ [e.target.name]: e.target.value });

  onSubmit = (e, token, user_id) => {
      e.preventDefault();
      axios.post('http://localhost:8000/api/login/', {
          username: this.state.email,
          password: this.state.password
      })
          .then(res => {
              this.setState({ user_id: res.data.user_id });
              this.setState({ token: res.data.token });
              this.setState({ redirect: './userlanding' });
              axios.get(`http://localhost:8000/api/users/${this.state.user_id}`)
                .then(res => this.setState({user_info: res.data}))
                .catch(err => console.log(err.response.data));
                this.setState({ email: '' });
                this.setState({ password: '' });
          })
          .catch(err => console.log(err.response));
  }

  render() {
    return (
      <Router>
        <Redirect to={this.state.redirect} />
        <div>
          <Route exact path='/' render={props => (
            <React.Fragment>
              <HeaderLanding />
              <Landing />
            </React.Fragment>
          )} />
          <Route path='/signup' render={props => (
            <React.Fragment>
              <FormHeader />
              <SignUp />
            </React.Fragment>
          )} />
          <Route path='/login' render={props => (
            <React.Fragment>
              <FormHeader />
              <LogIn onSubmit={this.onSubmit.bind(this)} onChange={this.onChange.bind(this)} redirect={this.state.redirect} />
            </React.Fragment>
          )} />
          <Route path='/signupconf' render={props => (
            <React.Fragment>
              <FormHeader />
              <SignUpConf />
            </React.Fragment>
          )} />
          <Route path='/userlanding' render={props => (
            <React.Fragment>
              <UserHeader token={this.state.token} user_id={this.state.user_id} signOut={this.signOut.bind(this)} />
              <UserLanding token={this.state.token} user_id={this.state.user_id} user={this.state.user_info} />
            </React.Fragment>
          )} />
          <Route path='/chats' render={props => (
            <React.Fragment>
              <UserHeader token={this.state.token} user_id={this.state.user_id} signOut={this.signOut.bind(this)} />
              <Chats token={this.state.token} user_id={this.state.user_id} user={this.state.user_info} />
            </React.Fragment>
          )} />
          <Route path='/vehicle' render={props => (
            <React.Fragment>
              <UserHeader token={this.state.token} user_id={this.state.user_id} signOut={this.signOut.bind(this)} />
              <VehicleRegister token={this.state.token} user_id={this.state.user_id} />
            </React.Fragment>
          )} />
          <Footer />
        </div>
      </Router>
    )
  }
}

export default App
