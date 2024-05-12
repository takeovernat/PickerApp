import * as React from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";

function createData(
  order_number,
  customer_name,
  title,
  order_date,
  location,
  status
) {
  return { order_number, customer_name, title, order_date, location, status };
}

// const rows = [
//   createData("1234", "john", "chiecken", "10/15/2022", "houston", "picked"),
//   createData("1234", "john", "chiecken", "10/15/2022", "houston", "picked"),
//   createData("1234", "john", "chiecken", "10/15/2022", "houston", "picked"),
//   createData("1234", "john", "chiecken", "10/15/2022", "houston", "picked"),
//   createData("1234", "john", "chiecken", "10/15/2022", "houston", "picked"),
// ];

export default function BasicTable({ report }) {
  let rows = [];

  const repo = report.filter((rep) => rep.pick_status != "picked");

  repo.forEach((rep) => {
    rows.push(
      createData(
        rep.order_number.order_number,
        rep.order_number.customer_name,
        rep.sku.title,
        rep.order_number.order_date,
        rep.sku.location_id,
        rep.pick_status
      )
    );
  });

  console.log("nate ", rows);
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell align="right">Order number</TableCell>
            <TableCell align="right">Customer name&nbsp;(g)</TableCell>
            <TableCell align="right">Title&nbsp;(g)</TableCell>
            <TableCell align="right">Order date&nbsp;(g)</TableCell>
            <TableCell align="right">Location&nbsp;(g)</TableCell>
            <TableCell align="right">Status&nbsp;(g)</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.name}
              sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
            >
              <TableCell align="right">{row.order_number}</TableCell>
              <TableCell align="right">{row.customer_name}</TableCell>
              <TableCell align="right">{row.title}</TableCell>
              <TableCell align="right">{row.order_date}</TableCell>
              <TableCell align="right">{row.location}</TableCell>
              <TableCell align="right">{row.status}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
