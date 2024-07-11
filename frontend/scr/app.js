import React from 'react';
import { Route, Switch } from 'react-router-dom';
import HomePage from './pages/HomePage';
import OrderPage from './pages/OrderPage';
import LoginPage from './pages/LoginPage';
import AdminDashboard from './pages/AdminDashboard';
import Header from './components/Header';
import Footer from './components/Footer';

function App() {
  return (
    <div>
      <Header />
      <div className="container">
        <Switch>
          <Route exact path="/" component={HomePage} />
          <Route path="/orders" component={OrderPage} />
          <Route path="/login" component={LoginPage} />
          <Route path="/admin" component={AdminDashboard} />
        </Switch>
      </div>
      <Footer />
    </div>
  );
}

export default App;
