import { useState, useEffect } from "react";
import Button from "./Button";
import BetBox from "./BetBox";

function Controller() {
  const [hasWon, setHasWon] =useState(false);

  const myFunc = () => {
    setHasWon(!hasWon);
  };


  useEffect(() => {
    console.log(hasWon);
  }, [hasWon]);

  return (
    <div className="w-full md:w-[850px0 lg:w-[1200px] py-12 bg-green-500 mx-auto px-5">
      <Button runFunction={myFunc} />
      <BetBox />
    </div>
  );
}

export default Controller