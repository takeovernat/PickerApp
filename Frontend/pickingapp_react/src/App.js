import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [picks, setPicks] = useState(0);
  const [orderlists, setOrderLists] = useState([]);
  const [orders, setOrders] = useState([]);
  const [orderlistsize, setOrderListSize] = useState(0);
  const [listindex, setListIndex] = useState(0);
  const [endoflist, setEndOfList] = useState(false);

  useEffect(() => {
    async function fetchOrderLists() {
      let response = await fetch("http://localhost:8000/orderlists/");
      response = await response.json();
      setOrderLists(response);
      setOrderListSize(response.length);
    }

    async function fetchOrders() {
      let res = await fetch("http://localhost:8000/orders/");
      res = await res.json();
      setOrders(res);
    }

    fetchOrderLists();
    fetchOrders();
  }, []);

  async function makeUpdateCall(url = "", data = {}) {
    const response = await fetch(url, {
      method: "PUT", // *GET, POST, PUT, DELETE, etc.
      mode: "cors", // no-cors, *cors, same-origin
      cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
      credentials: "same-origin", // include, *same-origin, omit
      headers: {
        "Content-Type": "application/json",
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      redirect: "follow", // manual, *follow, error
      referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
      body: data, // body data type must match "Content-Type" header
    });
    console.log(response.json);
    return response.json();
  }

  const handleException = (e) => {
    console.log(e);
    let url = "http://localhost:8000/orderlists/update/1";
    let reason = "unknown";
    const currentOrder = orderlists[listindex];
    let stock = currentOrder.sku.on_hand;
    console.log("jim ", stock);
    if (stock == 0 || stock < currentOrder.pick_quantity) {
      reason = "Not enough items in stock";
    }

    makeUpdateCall(url, `exception: ${reason}`);
  };

  const handlePick = () => {
    console.log("picked");
    setListIndex((prev) => prev + 1);
    console.log(orderlists);
    console.log(orderlistsize);
    console.log(listindex, orderlistsize);
    console.log((listindex + 1) / orderlistsize);
    console.log("tim", orders);

    if (listindex >= orderlistsize - 1) {
      setEndOfList(true);
    }
  };

  return (
    orderlists.length > 0 &&
    !endoflist && (
      <div className="flex items-center justify-center min-h-screen from-gray-800 via-greeen-300 to-blue-500 bg-gradient-to-br">
        <div className="w-full max-w-lg px-10 py-8 mx-auto bg-white rounded-lg shadow-xl">
          <div className="max-w-md mx-auto space-y-1">
            <h1 className="mb-4 font-extrabold text-4xl">pickingApp</h1>
            <progress className="" value={(listindex + 1) / orderlistsize} />
            <p className="text-sm">
              {listindex}/{orderlistsize} picks proccessed
            </p>

            <div className="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">
              <div className="inline-block mx-auto max-w-screen-sm text-center">
                <label>
                  <p className="mb-4 tracking-tight font-extrabold text-primary-600 dark:text-primary-500">
                    Location: {orderlists[listindex].location_id}
                    {/* <input className="border-2 ml-4" name="tim" /> */}
                  </p>
                </label>

                <label>
                  <p className="mb-4 tracking-tight font-extrabold text-primary-600 dark:text-primary-500">
                    SKU: {orderlists[listindex].sku.sku}
                    {/* <input className="border-2 ml-12" name="tim" /> */}
                  </p>
                </label>

                <label>
                  <p className="mb-4 tracking-tight font-extrabold text-primary-600 dark:text-primary-500">
                    Title: {orderlists[listindex].sku.title}
                    {/* <input className="border-2 ml-12" name="tim" /> */}
                  </p>
                </label>

                <label>
                  <p className="mb-4 tracking-tight font-extrabold text-primary-600 dark:text-primary-500">
                    Quantity: {orderlists[listindex].pick_quantity}
                    {/* <input className="border-2 ml-4" name="tim" /> */}
                  </p>
                </label>
                <div className="my-12">
                  <button
                    onClick={handlePick}
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 mx-5 rounded"
                  >
                    Pick
                  </button>
                  <button
                    onClick={handleException}
                    className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 mx-5 rounded"
                  >
                    Exception
                  </button>
                </div>
                {/* <p className="mb-4 text-3xl tracking-tight font-bold text-black md:text-4xl">
                Internal Server Error.
              </p>
              <p className="mb-4 text-lg font-light text-gray-500 dark:text-gray-400">
                We are already working to solve the problem.{" "}
              </p> */}
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  );
}

export default App;
