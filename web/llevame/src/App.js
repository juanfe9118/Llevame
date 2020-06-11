import React, { Component } from 'react';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import HeaderLanding from './components/layout/HeaderLanding';
import Footer from './components/layout/Footer';

import './App.css';

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <Route exact path='/' render={props => (
            <React.Fragment>
              <HeaderLanding />
            </React.Fragment>
          )} />
          <Footer />
        </div>
      </Router>
    )
  }
}

export default App
