import React from 'react';
import Loader from "react-loader-spinner";


export default function LoaderComponent() {

  return (
    <Loader
        type="ThreeDots"
        color="#000000"
        height={30}
        width={60}
      />
  );
}
