import React, { Component } from 'react';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import HeaderLanding from './components/layout/HeaderLanding';
import Footer from './components/layout/Footer';
import Landing from './components/layout/Landing';
import FormHeader from './components/layout/FormHeader';
import SignUp from './components/SignUp';
import LogIn from './components/LogIn';
import SignUpConf from './components/layout/SignUpConf';

import './App.css';

class App extends Component {
  state = {
    token: null,
    user_id: null,
  }
  render() {
    return (
      <Router>
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
              <LogIn />
          </React.Fragment>
          )} />
          <Route path='/signupconf' render={props => (
            <React.Fragment>
            <FormHeader />
            <SignUpConf />
          </React.Fragment>
          )} />
          <Footer />
        </div>
      </Router>
    )
  }
}

export default App
