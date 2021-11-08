import React, { useState, Fragment} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'
import './App.css'

import {HashRouter as Router, Route, Switch} from 'react-router-dom';

import Welcome from './components/Welcome';
import RoadMap from './components/RoadMap';
import Team from './components/Team';
import Mint from './components/Mint';
import AboutProject from './components/AboutProject'
import Routes from './Enums/Routes';
import NavComponent from './components/NavComponent';


const App = () => {

  const [walletAddress, setWalletAddress] = useState("");
  const [walletConnected, setWalletConnected] = useState(null);
  const [noWalletFound, setNoWalletFound] = useState(false);
  const [walletLoading, setWalletLoading] = useState(false);

  const connectWallet = () => {
    setWalletLoading(true);
    setNoWalletFound(false);


    if(window.ethereum){
      window.ethereum.request({method: 'eth_requestAccounts'})
      .then(result => {
        setConnectedWallet(result[0]);
      })
    }
    else{
      setWalletLoading(false);
      setNoWalletFound(true);
    }
  };

  const disconnectWallet = () => {
    setWalletAddress("");
    setWalletConnected(null);
    setNoWalletFound(false);
    setWalletLoading(false);
  };

  const setConnectedWallet = (account) => {
    if(account.length !== 0){
      setWalletAddress(account.slice(0,5) + "..." + account.slice(-4));
      setWalletConnected(account);
      setWalletLoading(false);
    }
    else{
      setWalletAddress("");
      setWalletConnected(null);
      setNoWalletFound(false);
      setWalletLoading(false);
    }
  }

  const chainChangedHandler = () =>{
    window.location.reload();
  }

  window.ethereum.on('accountsChanged', setConnectedWallet);
  window.ethereum.on('chainChanged', chainChangedHandler);

  return (
  <Router>
    <NavComponent connectWallet={connectWallet}
                  disconnectWallet={disconnectWallet}
                  noWalletFound={noWalletFound}
                  walletAddress={walletAddress}
                  walletLoading={walletLoading}
                  walletConnected={walletConnected}/>
    <Fragment>
      <Switch>
        <Route path={Routes.WELCOME} exact component={Welcome}></Route>
        <Route path={Routes.ABOUT_PROJECT} exact component={AboutProject}></Route>
        <Route path={Routes.ROADMAP} exact component={RoadMap}></Route>
        <Route path={Routes.TEAM} exact  component={Team}></Route>
        <Route path={Routes.MINT} exact  component={Mint}></Route>
      </Switch>
    </Fragment>
  </Router>) 
}

export default App;
