
import datetime
import isodate

import xmltodict

data = """<value>
    <struct>
     <member>
      <name>accountFlagsAfter</name>

      <value>

       <struct>

        <member>

         <name>activationStatusFlag</name>

         <value>

          <boolean>1</boolean>

         </value>

        </member>

        <member>

         <name>negativeBarringStatusFlag</name>

         <value>

          <boolean>0</boolean>

         </value>

        </member>

        <member>

         <name>serviceFeePeriodExpiryFlag</name>

         <value>

          <boolean>0</boolean>

         </value>

        </member>

        <member>

         <name>serviceFeePeriodWarningActiveFlag</name>

         <value>

          <boolean>0</boolean>

         </value>

        </member>

        <member>

         <name>supervisionPeriodExpiryFlag</name>

         <value>

          <boolean>0</boolean>

         </value>

        </member>

        <member>

         <name>supervisionPeriodWarningActiveFlag</name>

         <value>

          <boolean>0</boolean>

         </value>

        </member>

       </struct>

      </value>

     </member>

     <member>

      <name>accountFlagsBefore</name>

      <value>

       <struct>

        <member>

         <name>activationStatusFlag</name>

         <value>

          <boolean>1</boolean>

         </value>

        </member>

        <member>

         <name>negativeBarringStatusFlag</name>

         <value>

          <boolean>0</boolean>

         </value>

        </member>

        <member>

         <name>serviceFeePeriodExpiryFlag</name>

         <value>

          <boolean>0</boolean>

         </value>

        </member>

        <member>

         <name>serviceFeePeriodWarningActiveFlag</name>

         <value>

          <boolean>0</boolean>

         </value>

        </member>

        <member>

         <name>supervisionPeriodExpiryFlag</name>

         <value>

          <boolean>0</boolean>

         </value>

        </member>

        <member>

         <name>supervisionPeriodWarningActiveFlag</name>

         <value>

          <boolean>0</boolean>

         </value>

        </member>

       </struct>

      </value>

     </member>

     <member>

      <name>accountValue1</name>

      <value>

       <string>13600</string>

      </value>

     </member>

     <member>

      <name>availableServerCapabilities</name>

      <value>

       <array>

        <data>

         <value>

          <i4>537199172</i4>

         </value>

         <value>

          <i4>520</i4>

         </value>

        </data>

       </array>

      </value>

     </member>

     <member>

      <name>creditClearanceDate</name>

      <value>

       <dateTime.iso8601>20270212T12:00:00+0000</dateTime.iso8601>

      </value>

     </member>

     <member>

      <name>currency1</name>

      <value>

       <string>BDT</string>

      </value>

     </member>

     <member>

      <name>dedicatedAccountInformation</name>

      <value>

       <array>

        <data>

         <value>

          <struct>

           <member>

            <name>dedicatedAccountActiveValue1</name>

            <value>

             <string>6000</string>

            </value>

           </member>

           <member>

            <name>dedicatedAccountID</name>

            <value>

             <i4>207</i4>

            </value>

           </member>

           <member>

            <name>dedicatedAccountUnitType</name>

            <value>

             <i4>0</i4>

            </value>

           </member>

           <member>

            <name>dedicatedAccountValue1</name>

            <value>

             <string>6000</string>

            </value>

           </member>

           <member>

            <name>expiryDate</name>

            <value>

             <dateTime.iso8601>20230509T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

           <member>

            <name>startDate</name>

            <value>

             <dateTime.iso8601>00000101T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

          </struct>

         </value>

         <value>

          <struct>

           <member>

            <name>dedicatedAccountActiveValue1</name>

            <value>

             <string>0</string>

            </value>

           </member>

           <member>

            <name>dedicatedAccountID</name>

            <value>

             <i4>245</i4>

            </value>

           </member>

           <member>

            <name>dedicatedAccountUnitType</name>

            <value>

             <i4>1</i4>

            </value>

           </member>

           <member>

            <name>dedicatedAccountValue1</name>

            <value>

             <string>0</string>

            </value>

           </member>

           <member>

            <name>expiryDate</name>

            <value>

             <dateTime.iso8601>99991231T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

           <member>

            <name>startDate</name>

            <value>

             <dateTime.iso8601>00000101T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

          </struct>

         </value>

         <value>

          <struct>

           <member>

            <name>dedicatedAccountActiveValue1</name>

            <value>

             <string>0</string>

            </value>

           </member>

           <member>

            <name>dedicatedAccountID</name>

            <value>

             <i4>255</i4>

            </value>

           </member>

           <member>

            <name>dedicatedAccountUnitType</name>

            <value>

             <i4>1</i4>

            </value>

           </member>

           <member>

            <name>dedicatedAccountValue1</name>

            <value>

             <string>0</string>

            </value>

           </member>

           <member>

            <name>expiryDate</name>

            <value>

             <dateTime.iso8601>99991231T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

           <member>

            <name>startDate</name>

            <value>

             <dateTime.iso8601>00000101T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

          </struct>

         </value>

         <value>

          <struct>

           <member>

            <name>dedicatedAccountActiveValue1</name>

            <value>

             <string>5368709120</string>

            </value>

           </member>

           <member>

            <name>dedicatedAccountID</name>

            <value>

             <i4>303</i4>

            </value>

           </member>

           <member>

            <name>dedicatedAccountUnitType</name>

            <value>

             <i4>6</i4>

            </value>

           </member>

           <member>

            <name>dedicatedAccountValue1</name>

            <value>

             <string>5368709120</string>

            </value>

           </member>

           <member>

            <name>expiryDate</name>

            <value>

             <dateTime.iso8601>20230601T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

           <member>

            <name>startDate</name>

            <value>

             <dateTime.iso8601>00000101T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

          </struct>

         </value>

        </data>

       </array>

      </value>

     </member>

     <member>

      <name>languageIDCurrent</name>

      <value>

       <i4>1</i4>

      </value>

     </member>

     <member>

      <name>negotiatedCapabilities</name>

      <value>

       <array>

        <data>

         <value>

          <i4>536871492</i4>

         </value>

        </data>

       </array>

      </value>

     </member>

     <member>

      <name>offerInformationList</name>

      <value>

       <array>

        <data>

         <value>

          <struct>

           <member>

            <name>expiryDateTime</name>

            <value>

             <dateTime.iso8601>20230602T00:00:00+0600</dateTime.iso8601>

            </value>

           </member>

           <member>

            <name>offerID</name>

            <value>

             <i4>1563</i4>

            </value>

           </member>

           <member>

            <name>offerState</name>

            <value>

             <i4>0</i4>

            </value>

           </member>

           <member>

            <name>offerType</name>

            <value>

             <i4>2</i4>

            </value>

           </member>

           <member>

            <name>startDateTime</name>

            <value>

             <dateTime.iso8601>20230503T00:00:00+0600</dateTime.iso8601>

            </value>

           </member>

          </struct>

         </value>

         <value>

          <struct>

           <member>

            <name>expiryDate</name>

            <value>

             <dateTime.iso8601>20230509T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

           <member>

            <name>offerID</name>

            <value>

             <i4>3857</i4>

            </value>

           </member>

           <member>

            <name>offerType</name>

            <value>

             <i4>0</i4>

            </value>

           </member>

           <member>

            <name>startDate</name>

            <value>

             <dateTime.iso8601>20230503T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

          </struct>

         </value>

         <value>

          <struct>

           <member>

            <name>expiryDate</name>

            <value>

             <dateTime.iso8601>20230607T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

           <member>

            <name>offerID</name>

            <value>

             <i4>6608</i4>

            </value>

           </member>

           <member>

            <name>offerType</name>

            <value>

             <i4>0</i4>

            </value>

           </member>

           <member>

            <name>startDate</name>

            <value>

             <dateTime.iso8601>20230508T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

          </struct>

         </value>

         <value>

          <struct>

           <member>

            <name>expiryDate</name>

            <value>

             <dateTime.iso8601>99991231T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

           <member>

            <name>offerID</name>

            <value>

             <i4>10101</i4>

            </value>

           </member>

           <member>

            <name>offerType</name>

            <value>

             <i4>0</i4>

            </value>

           </member>

           <member>

            <name>startDate</name>

            <value>

             <dateTime.iso8601>20230123T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

          </struct>

         </value>

         <value>

          <struct>

           <member>

            <name>expiryDate</name>

            <value>

             <dateTime.iso8601>99991231T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

           <member>

            <name>offerID</name>

            <value>

             <i4>10102</i4>

            </value>

           </member>

           <member>

            <name>offerType</name>

            <value>

             <i4>0</i4>

            </value>

           </member>

           <member>

            <name>startDate</name>

            <value>

             <dateTime.iso8601>20230123T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

          </struct>

         </value>

         <value>

          <struct>

           <member>

            <name>expiryDate</name>

            <value>

             <dateTime.iso8601>99991231T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

           <member>

            <name>offerID</name>

            <value>

             <i4>10103</i4>

            </value>

           </member>

           <member>

            <name>offerType</name>

            <value>

             <i4>0</i4>

            </value>

           </member>

           <member>

            <name>startDate</name>

            <value>

             <dateTime.iso8601>20230123T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

          </struct>

         </value>

         <value>

          <struct>

           <member>

            <name>expiryDate</name>

            <value>

             <dateTime.iso8601>99991231T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

           <member>

            <name>offerID</name>

            <value>

             <i4>10105</i4>

            </value>

           </member>

           <member>

            <name>offerType</name>

            <value>

             <i4>0</i4>

            </value>

           </member>

           <member>

            <name>startDate</name>

            <value>

             <dateTime.iso8601>20230123T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

          </struct>

         </value>

         <value>

          <struct>

           <member>

            <name>expiryDate</name>

            <value>

             <dateTime.iso8601>20230601T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

           <member>

            <name>offerID</name>

            <value>

             <i4>21035</i4>

            </value>

           </member>

           <member>

            <name>offerType</name>

            <value>

             <i4>0</i4>

            </value>

           </member>

           <member>

            <name>startDate</name>

            <value>

             <dateTime.iso8601>20230503T12:00:00+0000</dateTime.iso8601>

            </value>

           </member>

          </struct>

         </value>

        </data>

       </array>

      </value>

     </member>

     <member>

      <name>originTransactionID</name>

      <value>

       <string>2023050812502975</string>

      </value>

     </member>

     <member>

      <name>responseCode</name>

      <value>

       <i4>0</i4>

      </value>

     </member>

     <member>

      <name>serviceClassCurrent</name>

      <value>

       <i4>146</i4>

      </value>

     </member>

     <member>

      <name>serviceFeeExpiryDate</name>

      <value>

       <dateTime.iso8601>20330429T12:00:00+0000</dateTime.iso8601>

      </value>

     </member>

     <member>

      <name>serviceRemovalDate</name>

      <value>

       <dateTime.iso8601>20351016T12:00:00+0000</dateTime.iso8601>

      </value>

     </member>

     <member>

      <name>supervisionExpiryDate</name>

      <value>

       <dateTime.iso8601>20240425T12:00:00+0000</dateTime.iso8601>

      </value>

     </member>

    </struct>

   </value>

  </param>

 </params>

</methodResponse>

"""

# print(data)
# o = xmltodict.parse(data)
# print(o)
def _convert_start_date(start_date):
    """
    Fix year 1970 to month start date bill period
    """
    if '0000' == str(start_date)[:4]:
        today = datetime.datetime.utcnow()
        new_start = today.replace(
            day=1, hour=0, minute=0,
            second=0, microsecond=0)
        # is UTC
        print('innn')
        return new_start.isoformat() + '+00:00'

    start_date = isodate.parse_datetime(str(start_date))
    return start_date.isoformat()[:-6] + '+00:00'

response = {
        'offerInformationList': [
            {
                'expiryDateTime': '20230602T00:00:00+0600'
            },
            {
                'expiryDate': '20230509T12:00:00+0000'
            }
        ]
    }


def _set_datetime_or_date(key, pattern, obj):
    if pattern in obj:
        obj[key] = _convert_start_date(obj.pop(pattern))

    else:
        obj[key] = _convert_start_date(obj.pop("%sTime" % pattern))


print(response)
if 'offerInformationList' in response:
    for offerinfo in response["offerInformationList"]:
        # _set_datetime_or_date(
        #     'startDateTime', 'startDate', offerinfo)
        _set_datetime_or_date(
            'expiryDateTime', 'expiryDate', offerinfo)

print(response)

ls ='20230602T00:00:00+0600'
#ls = '20230601T12:00:00+0000'
ls = '2023-05-09T12:49:37+06:00'
print(_convert_start_date(ls))

#2023-06-02T00:00:00+00:00
#2023-06-01T12:00:00+00:00