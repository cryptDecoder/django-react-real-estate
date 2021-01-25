import React from 'react'
import Layout  from './hocs/Layout'
import { BrowserRouter as Router, Route, Switch} from 'react-router-dom'
import Home from './container/Home'
import About from './container/About'
import Contact from  './container/Contact'
import ListingDetails from './container/ListingDetails'
import Listings from './container/Listings'
import Login from './container/Login'
import SignUp from './container/SignUp'
import NotFound from './components/404'
import './sass/main.scss';
import { provider } from 'react-redux'
import store from './store'


const App = ()=>(
  <provider>
    <Router>
      <Layout>
        <Switch>
          <Route exact path="/" component={Home}></Route>
          <Route exact path="/about" component={About}></Route>
          <Route exact path="/contact" component={Contact}></Route>
          <Route exact path="/listings" component={Listings}></Route>\
          <Route exact path="/listings/:id" component={ListingDetails}></Route>
          <Route exact path="/login" component={Login}></Route>
          <Route exact path="/Signup" component={SignUp}></Route>
          <Route component={NotFound}></Route>
        </Switch>
      </Layout>
    </Router>
  </provider>
  
  
);
  

export default App;
