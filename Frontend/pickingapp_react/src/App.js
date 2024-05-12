import { useState, useEffect } from "react";
import "./App.css";
import { makeUpdateCall, fetchLinesbyOrder } from "./utils";
import Alert from "@mui/material/Alert";
import CheckIcon from "@mui/icons-material/Check";
import ErrorIcon from "@mui/icons-material/Error";
import NavigateNextIcon from "@mui/icons-material/NavigateNext";
import NavigateBeforeIcon from "@mui/icons-material/NavigateBefore";

function App() {
  const [failedpicks, setFailedPicks] = useState([]);
  const [picks, setPicks] = useState([]);
  const [orderlists, setOrderLists] = useState([]);
  const [orders, setOrders] = useState([]);
  const [orderlistsize, setOrderListSize] = useState(0);
  const [listindex, setListIndex] = useState(-1);
  const [endoflist, setEndOfList] = useState(false);
  const [proccessed, setProccessed] = useState(false);
  const [colorOfCard, setColorOfCard] = useState("bg-gray-100");
  const [exception, setException] = useState(false);
  const [reporttoggle, setReportToggle] = useState(false);
  const [report, setReport] = useState([]);
  const [showBtn, setShowBtn] = useState(true);

  //inital calls to get orders and orderlines
  useEffect(() => {
    async function fetchOrderLists() {
      let response = await fetch("http://localhost:8000/orderlines/");
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
  }, [proccessed]);

  // const fetchCurrentScreen = (id) => {
  //   fetch(`http://localhost:8000/orderlines/${id}`)
  //     .then((res) => res.json())
  //     .then((data) => {
  //       console.log(data);
  //       if (data.pick_status == "picked") {
  //         setColorOfCard("bg-green-50");
  //         setException(false);
  //       } else {
  //         setColorOfCard("bg-red-50");
  //         setException(true);
  //       }
  //     });
  // };

  const handlePrevious = () => {
    console.log(orderlists);
    setListIndex((prev) => prev + 1);
    setShowBtn(false);
  };

  function setStatus(status) {
    if (status == "picked") {
      setException(false);
      setColorOfCard("bg-green-50");
    } else {
      setException(true);
      setColorOfCard("bg-red-50");
    }
  }

  const handleNext = (e) => {
    console.log(exception);
    console.log(proccessed);
    console.log(listindex);
    console.log(orderlists[listindex]);
    if (listindex == 0) {
      fetch("http://localhost:8000/orderlines/")
        .then((res) => res.json())
        .then((data) => setOrderLists(data));
    }
    if (listindex >= orderlistsize - 1) {
      setListIndex(0);
      // fetchCurrentScreen(orderlists[0].id);
      let status = orderlists[0].pick_status;
      setStatus(status);
    } else {
      setListIndex((prev) => prev + 1);
      let status = orderlists[listindex + 1].pick_status;
      setStatus(status);
    }
  };

  const handleProcess = (e) => {
    let targetId = e.target.value;
    if (targetId == -1) {
      setListIndex((prev) => prev + 1);
    }

    console.log(listindex, orderlistsize);
    console.log((listindex + 1) / orderlistsize);
    // console.log("orders", orders);

    function handlelines(linesbyOrder, order_number) {
      linesbyOrder.forEach((line) => {
        // console.log("processing: ", line);
        async function getProduct() {
          let product = await fetch(
            `http://localhost:8000/productmaster/${line.sku.sku}`
          );
          product = await product.json();
          //check for 404
          return product;
        }

        getProduct().then((res) => {
          if (
            res.on_hand >= line.pick_quantity &&
            res.location_id == line.location_id
          ) {
            setPicks((prev) => [...prev, line.id]);

            makeUpdateCall(
              `http://localhost:8000/orderlines/update/${line.id}`,
              "picked"
            );
          } else if (res.location_id != line.location_id) {
            makeUpdateCall(
              `http://localhost:8000/orderlines/update/${line.id}`,
              "exception: item not available at location"
            );
          } else if (res.on_hand < line.pick_quantity) {
            setFailedPicks((prev) => [...prev, line.id]);
            makeUpdateCall(
              `http://localhost:8000/orderlines/update/${line.id}`,
              "exception: not enough items in stock"
            );
          }
        });

        makeUpdateCall(
          `http://localhost:8000/productmaster/update/${line.sku.sku}`,
          line.pick_quantity
        ).catch((err) => console.log(err));
      });
    }

    orders.forEach((o) => {
      fetchLinesbyOrder(o.order_number)
        .then((data) => {
          handlelines(data, o.order_number);
        })
        .then((d) => {
          setProccessed(true);
        });
    });

    if (listindex >= orderlistsize - 1) {
      setEndOfList(true);
    }

    // console.log("inex ", listindex);
    // console.log("od ", orderlists);
  };

  function handleReport() {
    console.log("report", picks);

    fetch("http://localhost:8000/orderlines/regected")
      .then((res) => res.json())
      .then((data) => setReport(data));

    setReportToggle((prev) => !prev);
  }

  return (
    orderlists.length > 0 &&
    !endoflist && (
      <div className="flex items-center justify-center min-h-screen from-gray-800 via-greeen-300 to-blue-500 bg-gradient-to-br">
        <div className="w-full max-w-lg px-10 py-8 mx-auto bg-white rounded-lg shadow-xl">
          <div className="max-w-md mx-auto space-y-1">
            <h1 className="mb-4 font-extrabold text-4xl">pickingApp</h1>
            <progress className="" value={(listindex + 1) / orderlistsize} />
            <p className="text-sm">
              {listindex + 1}/{orderlistsize} picks proccessed
            </p>

            <div className="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">
              {listindex != -1 && (
                <div
                  className={`inline-block mx-auto max-w-screen-sm text-center w-full ${colorOfCard}`}
                >
                  <label>
                    <p className="mb-4 tracking-tight font-extrabold text-primary-600 dark:text-primary-500">
                      Location:{" "}
                      {listindex >= 0
                        ? orderlists[listindex].location_id
                        : "..."}
                      {/* <input className="border-2 ml-4" name="tim" /> */}
                    </p>
                  </label>

                  <label>
                    <p className="mb-4 tracking-tight font-extrabold text-primary-600 dark:text-primary-500">
                      SKU:{" "}
                      {listindex >= 0 ? orderlists[listindex].sku.sku : "..."}
                      {/* <input className="border-2 ml-12" name="tim" /> */}
                    </p>
                  </label>

                  <label>
                    <p className="mb-4 tracking-tight font-extrabold text-primary-600 dark:text-primary-500">
                      Title:{" "}
                      {listindex >= 0 ? orderlists[listindex].sku.title : "..."}
                      {/* <input className="border-2 ml-12" name="tim" /> */}
                    </p>
                  </label>

                  <label>
                    <p className="mb-4 tracking-tight font-extrabold text-primary-600 dark:text-primary-500">
                      Quantity:{" "}
                      {listindex >= 0
                        ? orderlists[listindex].pick_quantity
                        : "..."}
                      {/* <input className="border-2 ml-4" name="tim" /> */}
                    </p>
                  </label>
                  <div className="my-2"></div>
                </div>
              )}
              <div className="mt-5">
                {exception && listindex >= 0 && (
                  <Alert
                    icon={<ErrorIcon fontSize="inherit" />}
                    severity="error"
                  >
                    {orderlists[listindex].pick_status}
                  </Alert>
                )}
                {!exception &&
                  listindex >= 0 &&
                  orderlists[listindex].pick_status == "picked" && (
                    <Alert
                      icon={<CheckIcon fontSize="inherit" />}
                      severity="success"
                    >
                      Picked
                    </Alert>
                  )}
              </div>
              <div className="mt-10 flex justify-end">
                {proccessed && showBtn && (
                  <button
                    // disabled={true}
                    onClick={handlePrevious}
                    className="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded"
                  >
                    show cards
                  </button>
                )}
                {proccessed && listindex != -1 && (
                  <button
                    onClick={handleNext}
                    className="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 mx-5 rounded"
                  >
                    <NavigateNextIcon></NavigateNextIcon>
                  </button>
                )}
              </div>
              <div className="w-full block m-auto">
                {proccessed && (
                  <button
                    onClick={handleReport}
                    className="block mt-16 bg-gray-500 hover:bg-gray-700 text-white  my-3 rounded"
                  >
                    Report
                  </button>
                )}
              </div>
              {reporttoggle && (
                <div>
                  <h3 className="mb-3 text-lg font-bold">
                    successfull processed {picks.length} / {orderlists.length}{" "}
                    order lines
                  </h3>
                  <h3 className="mb-3 text-lg font-bold">
                    Unsuccessful Orders:
                  </h3>
                  {report.length == 0 && <p>All orderslines succeded</p>}

                  {report.map((rep) => (
                    <div className="mb-3">
                      <p>Order Number: {rep.order_number.order_number}</p>
                      <p>Customer Name: {rep.order_number.customer_name}</p>
                      <p>Title: {rep.sku.title}</p>
                      <p>Order Date: {rep.order_number.order_date}</p>
                      <p>Location: {rep.sku.location_id}</p>
                      <p>{rep.pick_status}</p>
                    </div>
                  ))}
                </div>
              )}

              {!proccessed && (
                <button
                  onClick={handleProcess}
                  value={listindex >= 0 ? orderlists[listindex].id : ""}
                  className="block mt-16 bg-gray-400 hover:bg-gray-700 text-white font-bold py-2 px-4 mx-5 rounded w-11/12"
                >
                  Process picks
                </button>
              )}
            </div>
          </div>
        </div>
      </div>
    )
  );
}

export default App;
