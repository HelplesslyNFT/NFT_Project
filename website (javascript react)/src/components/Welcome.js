import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Button} from '@material-ui/core';
import { Link as Scroll } from 'react-scroll';

import Sections from '../Enums/Routes';
import Colors from '../Enums/Colors';

export default function Welcome() {
  const classes = useStyles();

  return (
    <div className={classes.root} id={Sections.WELCOME}>
        <div className={classes.container}>
          <h1 className={classes.title}>
            Welcome to <br />
            My<span className={classes.colorText}>Project.</span>
          </h1>
          <Scroll to={Sections.ABOUT_PROJECT} smooth={true}>
            <Button variant="outlined">
            <span className={classes.colorText}>Learn More</span>
            </Button>
          </Scroll>
        </div>
    </div>
  );
}

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    height: '100vh',
    fontFamily: 'Nunito',
    background: Colors.PRIMARY
  },
  icon: {
    color: '#fff',
    fontSize: '2rem',
  },
  colorText: {
    color: '#5AFF3D',
  },
  container: {
    textAlign: 'center',
  },
  title: {
    color: '#fff',
    fontSize: '4.5rem',
  },
  goDown: {
    color: '#5AFF3D',
    fontSize: '4rem',
  },
}));