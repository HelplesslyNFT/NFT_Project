import React, { Fragment, Component } from 'react'
import { Navbar, Nav } from 'react-bootstrap'
import {Link} from "react-router-dom";
import {Button} from "@material-ui/core"
import './NavComponent.css'

import Routes from '../Enums/Routes';
import LoaderComponent from "./LoaderComponent";

export default class NavComponent extends Component {
    render() {

        let {connectWallet, disconnectWallet, noWalletFound, walletAddress, walletLoading, walletConnected} = this.props; 
        
        return (
                <div>
                    <Navbar bg="transparent" variant="light" expand="lg">
                        <Navbar.Brand href="#">My Project</Navbar.Brand>
                        <Navbar.Toggle aria-controls="basic-navbar-nav" />
                        <Navbar.Collapse id="basic-navbar-nav">
                            <Nav
                                className="me-auto"
                            >
                                <Nav.Link as={Link} to={Routes.WELCOME}>Home</Nav.Link>
                                <Nav.Link as={Link} to={Routes.ABOUT_PROJECT}>About</Nav.Link>
                                <Nav.Link as={Link} to={Routes.ROADMAP}>RoadMap</Nav.Link>
                                <Nav.Link as={Link} to={Routes.TEAM}> Team</Nav.Link>
                                <Nav.Link as={Link} to={Routes.MINT}> Mint</Nav.Link>
                                {/* //TODO ADD TEAM AND MINT PAGES! */}
                                <Button 
                                    variant={"outlined"} 
                                    onClick={walletConnected !== null ? disconnectWallet : connectWallet} 
                                    children={walletLoading ?
                                        <LoaderComponent/>
                                        :
                                        walletConnected !== null ?
                                        <Fragment>Disconnect Wallet</Fragment>
                                            :
                                        <Fragment>Connect Wallet</Fragment>}>
                                    </Button>
                                {walletAddress !== "" ?<Navbar.Text> {walletAddress} </Navbar.Text> : null}
                                {noWalletFound ? <Fragment>Please install Metamask</Fragment> : null}
                            </Nav>
                        </Navbar.Collapse>
                    </Navbar>
                </div>
        )
    }
}